from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from toy.models import Toy
from django.db.models import Q

# Create your views here.


def index(request):
    return render(request, 'index.template.html')


def add_to_cart(request, toy_id):
    # attempt to get existing cart from the session using the key "shopping_cart"
    # the second argument will be the default value if
    # if the key does not exist in the session
    cart = request.session.get('shopping_cart', {})

    # we check if the toy_is not in the cart. If so, we will add it
    if toy_id not in cart:
        toy = get_object_or_404(Toy, pk=toy_id)
        # toy is found, let's add it to the cart
        cart[toy_id] = {
            'id': toy_id,
            'title': toy.title,
            'price': 99,
            'qty': 1
        }

        # save the cart back to sessions
        request.session['shopping_cart'] = cart

        messages.success(request, "Toy has been added to your cart!")
        return redirect(reverse('show_toy_route'))
    else:
        cart[toy_id]['qty'] += 1
        request.session['shopping_cart'] = cart
        return redirect(reverse('show_toy_route'))
