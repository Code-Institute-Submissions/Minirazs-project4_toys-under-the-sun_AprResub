from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .forms import ToyForm, EditToyForm, SearchForm
from .models import Toy
from django.db.models import Q


def redirect_view(request):
    response = redirect('/toy/')
    return response


def index(request):
    toys = Toy.objects.all()
    search_form = SearchForm()

    return render(request, 'toy/index.template.html', {
        'toys': toys,
        'search_form': search_form
    })


def search(request):

    toy_query = Toy.objects.all()

    search_form = SearchForm()

    queries = ~Q(pk__in=[])

    if request.GET:

        if 'title' in request.GET and request.GET['title'] and request.GET['title'] != "":
            queries = queries & Q(title__icontains=request.GET['title'])

        if 'age' in request.GET and request.GET['age']:
            queries = queries & Q(age__in=request.GET.getlist('age'))

        if 'country' in request.GET and request.GET['country']:
            queries = queries & Q(country__in=request.GET.getlist('country'))

        if 'category' in request.GET and request.GET['category']:
            queries = queries & Q(category__in=request.GET.getlist('category'))

    all_toys = toy_query.filter(queries)

    for i in all_toys:
        i.price = float(i.price/100)

    return render(request, 'toy/search.template.html', {
        'toys': all_toys,
        'search_form': search_form
    })


def one_toy(request, toy_id):
    toy = get_object_or_404(Toy, pk=toy_id)

    toy.price = float(toy.price/100)

    return render(request, 'toy/one_toy.template.html', {
        'toy': toy
    })


@staff_member_required
def create_toy(request):
    if request.method == 'POST':

        create_form = ToyForm(request.POST)

        if create_form.is_valid():
            create_form.save()
            messages.success(
                request,
                f"New toy {create_form.cleaned_data['title']} is created"
            )
            return redirect(reverse(index))
        else:
            return render(request, 'toy/create.template.html', {
                'form': create_form
            })
    else:
        create_form = ToyForm()
        return render(request, 'toy/create.template.html', {
            'form': create_form
        })


@staff_member_required
def update_toy(request, toy_id):

    toy_being_updated = get_object_or_404(Toy, pk=toy_id)

    if request.method == "POST":
        toy_form = ToyForm(request.POST, instance=toy_being_updated)

        if toy_form.is_valid():
            toy_form.save()
            return redirect(reverse(index))

        else:
            return render(request, 'toy/update.template.html', {
                "form": toy_form
            })
    else:
        toy_form = EditToyForm(instance=toy_being_updated)

        return render(request, 'toy/update.template.html', {
            "form": toy_form,
        })


@staff_member_required
def delete_toy(request, toy_id):

    if request.method == 'POST':
        toy_to_delete = get_object_or_404(Toy, pk=toy_id)
        toy_to_delete.delete()
        return redirect(index)
    else:
        toy_to_delete = get_object_or_404(Toy, pk=toy_id)
        return render(request, 'toy/delete.template.html', {
            "toy": toy_to_delete
        })
