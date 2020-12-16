from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Toy
from .forms import ToyForm

# Create your views here.


def index(request):
    toys = Toy.objects.all()

    return render(request, 'toys/index.template.html', {
        'toys': toys
    })


def create_toy(request):
    if request.method == 'POST':  # 1

        create_form = ToyForm(request.POST)  # 2

        # check if the form has valid values
        if create_form.is_valid():  # 3
            create_form.save()  # 4
            return redirect(reverse(index))
        else:
            # 5. if does not have valid values, re-render the form
            return render(request, 'toys/create.template.html', {
                'form': create_form
            })
    else:
        create_form = ToyForm()
        return render(request, 'toys/create.template.html', {
            'form': create_form
        })
