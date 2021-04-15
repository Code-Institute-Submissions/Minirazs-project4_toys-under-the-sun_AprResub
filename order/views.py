from django.shortcuts import render
from .models import Order


def index(request):

    orders = Order.objects.all()

    return render(request, 'order/index.template.html', {
        'orders': orders
    })
