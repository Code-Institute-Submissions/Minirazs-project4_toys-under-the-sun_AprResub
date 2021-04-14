from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from toy.models import Toy
from django.db.models import Q

# Create your views here.


@login_required
def add_to_cart(request, toy_id):
    # attempt to get existing cart from session using the key "shopping_cart"
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
            'price': float(toy.price/100),
            'qty': 1,
            'cover': str(toy.cover),
            # calculate subtotal of the toy
            'total': float(toy.price/100)
        }

        # save the cart back to sessions
        request.session['shopping_cart'] = cart

        messages.success(request, f"{toy.title} has been added to your cart!")
        return redirect(reverse('show_toy_route'))
    else:
        cart[toy_id]['qty'] += 1
        cart[toy_id]['total'] = int(
            cart[toy_id]['qty']) * float(cart[toy_id]['price'])
        request.session['shopping_cart'] = cart
        messages.success(request, f"{cart[toy_id]['title']} "
                                  f"has been added to your cart!")
        return redirect(reverse('show_toy_route'))


@login_required
def view_cart(request):
    # retrieve the cart
    cart = request.session.get('shopping_cart', {})
    grand_total = 0
    print(cart)
    for k, v in cart.items():
        grand_total += v['total']

    return render(request, 'cart/view_cart.template.html', {
        'cart': cart,
        'grand_total': grand_total
    })


@login_required
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


@login_required
def update_quantity(request, toy_id):
    cart = request.session.get('shopping_cart')
    if toy_id in cart:
        # update quantity
        cart[toy_id]['qty'] = request.POST['qty']

        # update cart subtotal
        cart[toy_id]['total'] = int(
            cart[toy_id]['qty']) * float(cart[toy_id]['price'])

    # Tally grand total
    print(cart)
    grand_total = 0
    for k, v in cart.items():
        grand_total += v['total']

    # Save session
    request.session['shopping_cart'] = cart
    messages.success(
        request, f"Quantity for {cart[toy_id]['title']} has been changed")

    return render(request, 'cart/view_cart.template.html', {
        'cart': cart,
        'grand_total': grand_total
    })
