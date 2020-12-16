from django.shortcuts import render, HttpResponse
from .models import Toy

# Create your views here.


def index(request):
    toys = Toy.objects.all()

    return render(request, 'toys/index.template.html', {
        'toys': toys
    })
