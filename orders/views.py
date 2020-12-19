from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Order


# Create your views here.
def index(request):

    orders = Order.objects.all()

    return render(request, 'orders/index.template.html', {
        'orders': orders
    })