from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from toy.models import Toy
from django.db.models import Q

# Create your views here.


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
            'price': float(toy.price),
            'qty': 1
        }

        # save the cart back to sessions
        request.session['shopping_cart'] = cart

        messages.success(request, f"{toy.title} has been added to your cart!")
        return redirect(reverse('show_toy_route'))
    else:
        cart[toy_id]['qty'] += 1
        request.session['shopping_cart'] = cart
        return redirect(reverse('show_toy_route'))


def view_cart(request):
    # retrieve the cart
    cart = request.session.get('shopping_cart', {})

    return render(request, 'cart/view_cart.template.html', {
        'shopping_cart': cart
    })


def remove_from_cart(request, toy_id):
    # retrieve the cart from session
    cart = request.session.get('shopping_cart', {})

    # if the book is in the cart
    if toy_id in cart:
        # remove it from the cart
        del cart[toy_id]
        # save back to the session
        request.session['shopping_cart'] = cart
        messages.success(request, "Item removed from cart successfully!")

    return redirect(reverse('show_toy_route'))


def update_quantity(request, toy_id):
    cart = request.session.get('shopping_cart')
    if toy_id in cart:
        cart[toy_id]['qty'] = request.POST['qty']
        request.session['shopping_cart'] = cart
        messages.success(request, f"Quantity for {cart[toy_id]['title']} has been changed")
    
    return redirect(reverse('view_cart_route'))
