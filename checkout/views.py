from django.shortcuts import render, get_object_or_404, reverse, HttpResponse
from django.conf import settings
from django.contrib.sites.models import Site
from toy.models import Toy
from .models import Purchase
import stripe
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def checkout(request):
    # set the api keys for stripe to work
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # retrieve the shopping cart
    cart = request.session.get('shopping_cart', {})

    line_items = []
    all_toy_ids = []

    # go through each item in the shopping cart
    for toy_id, cart_item in cart.items():

        # retrieve the toy specified by toy_id
        toy_model = get_object_or_404(Toy, pk=toy_id)

        # create the line item
        # for the line item, each key in the dictionary is prefixed by Stripes
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

    # create a payment session (it's for Stripe)
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


def checkout_success(request):
    # Empty the shopping cart
    request.session['shopping_cart'] = {}

    return HttpResponse("Payment completed successfully")


def checkout_cancelled(request):
    return HttpResponse("Checkout cancelled")


@csrf_exempt
def payment_completed(request):

    endpoint_secret = settings.ENDPOINT_SECRET
    payload = request.body

    # retrieve the signature sent from Stripe
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )

    except ValueError as e:
        # Invalid payload
        print("Invalid payload")
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Signature is invalid
        print("Invalid signature")
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        handle_payment(session)

    print(request.body)

    return HttpResponse(status=200)


def handle_payment(session):
    print(session)
