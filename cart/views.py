from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from toy.models import Toy


@login_required
def add_to_cart(request, toy_id):
    cart = request.session.get('shopping_cart', {})

    if toy_id not in cart:
        toy = get_object_or_404(Toy, pk=toy_id)

        cart[toy_id] = {
            'id': toy_id,
            'title': toy.title,
            'price': float(toy.price/100),
            'qty': 1,
            'cover': str(toy.cover),
            'total': float(toy.price/100)
        }

        request.session['shopping_cart'] = cart

        messages.success(
            request, f"{toy.title} has been added to your cart!")
        return redirect(reverse('search_toy'))
    else:
        cart[toy_id]['qty'] += 1
        cart[toy_id]['total'] = int(
            cart[toy_id]['qty']) * float(cart[toy_id]['price'])
        request.session['shopping_cart'] = cart
        messages.success(request, f"{cart[toy_id]['title']} "
                                  f"has been added to your cart!")
        return redirect(reverse('search_toy'))


@login_required
def view_cart(request):

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

    cart = request.session.get('shopping_cart', {})

    if toy_id in cart:

        del cart[toy_id]

        request.session['shopping_cart'] = cart
        messages.success(request, "Item removed from cart successfully!")

    return redirect(reverse('view_cart_route'))


@login_required
def update_quantity(request, toy_id):
    cart = request.session.get('shopping_cart')
    if toy_id in cart:
        cart[toy_id]['qty'] = request.POST['qty']

        cart[toy_id]['total'] = int(
            cart[toy_id]['qty']) * float(cart[toy_id]['price'])

    grand_total = 0
    for k, v in cart.items():
        grand_total += v['total']

    request.session['shopping_cart'] = cart
    messages.success(
        request, f"Quantity for {cart[toy_id]['title']} has been changed")

    return render(request, 'cart/view_cart.template.html', {
        'cart': cart,
        'grand_total': grand_total
    })
