from .forms import ToyForm
from .models import Toy
from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404

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


def update_toy(request, toy_id):
    # 1. retrieve the toy which we are editing
    toy_being_updated = get_object_or_404(Toy, pk=toy_id)

    # 2 - create the form and fill it with data from toy instance
    toy_form = ToyForm(instance=toy_being_updated)

    return render(request, 'toys/update.template.html', {
        "form": toy_form
    })
