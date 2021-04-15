from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from toy.models import Toy
from .models import Purchase
import stripe
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('shopping_cart', {})

    line_items = []
    all_toy_ids = []

    for toy_id, cart_item in cart.items():

        toy_model = get_object_or_404(Toy, pk=toy_id)

        item = {
            "name": toy_model.title,
            "amount": int(toy_model.price),
            "quantity": cart_item['qty'],
            "currency": 'sgd'
        }

        line_items.append(item)
        all_toy_ids.append({
            'toy_id': toy_model.id,
            'qty': cart_item['qty']
        })

    current_site = Site.objects.get_current()
    domain = current_site.domain

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=line_items,
        client_reference_id=request.user.id,
        metadata={
            'all_toy_ids': json.dumps(all_toy_ids)
        },
        mode="payment",
        success_url=domain + reverse('checkout_success'),
        cancel_url=domain + reverse('checkout_cancelled')
    )

    return render(request, "checkout/checkout.template.html", {
        'session_id': session.id,
        'public_key': settings.STRIPE_PUBLISHABLE_KEY
    })


@login_required
def checkout_success(request):
    request.session['shopping_cart'] = {}
    messages.success(request, "Payment is successful!")
    return redirect(reverse("home"))


@login_required
def checkout_cancelled(request):
    messages.error(request, "Payment is unsuccessful! Please try again!")
    return redirect(reverse("view_cart_route"))


@csrf_exempt
def payment_completed(request):

    endpoint_secret = settings.ENDPOINT_SECRET
    payload = request.body

    sig_header = request.META['HTTP_STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )

    except ValueError as e:
        print("Invalid payload")
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:

        print("Invalid signature")
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        handle_payment(session)

    return HttpResponse(status=200)


@login_required
def handle_payment(session):

    metadata = session['metadata']
    all_toy_ids = json.loads(metadata['all_toy_ids'])

    user = get_object_or_404(User, pk=session['client_reference_id'])

    for toy_ordered in all_toy_ids:
        toy_model = get_object_or_404(Toy, pk=toy_ordered['toy_id'])

        purchase = Purchase()
        purchase.toy = toy_model
        purchase.user = user
        purchase.qty = toy_ordered['qty']
        purchase.price = toy_model.price

        purchase.save()
