from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Review
from .forms import ReviewForm
from toys.models import Toy

# Create your views here.


def index(request):
    reviews = Review.objects.all()

    return render(request, 'reviews/index.template.html', {
        'reviews': reviews
    })


@login_required
def create_review(request, toy_id):
    toy = get_object_or_404(Toy, pk=toy_id)

    if request.method == "POST":
        # fill in the form with what the user has typed in
        form = ReviewForm(request.POST)
        if form.is_valid():
            # save the form it will the create model instance
            # i.e it will insert the new row into the table in the database
            # when we specify Commit=False, means don't save to database
            review = form.save(commit=False)
            review.user = request.user  # request.user contain logged in user
            review.toy = toy
            review.save()
            messages.success(request, "New review added!")
            return redirect(index)
    else:
        form = ReviewForm()
        return render(request, 'reviews/create.template.html', {
            'form': form,
            'toy': toy
        })


@login_required
def update_review(request, review_id):
    # 1. retrieve the review which we are editing
    review_being_updated = get_object_or_404(Review, pk=review_id)

    # 2 - create the form and fill it with data from review instance
    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review_being_updated)

        # 3. create the form and fill in the user's data. Also specify that
        # this is to update an existing model (the instance argument)
        if review_form.is_valid():
            review_form.save()
            return redirect(reverse(index))

        else:
            return render(request, 'reviews/update.template.html', {
                "form": review_form
            })
    else:
        # 4. create a form with the review details filled in
        review_form = ReviewForm(instance=review_being_updated)

        return render(request, 'reviews/update.template.html', {
            "form": review_form
        })


@login_required
def delete_review(request, review_id):

    if request.method == 'POST':
        review_to_delete = get_object_or_404(Review, pk=review_id)
        review_to_delete.delete()
        return redirect(index)
    else:
        review_to_delete = get_object_or_404(Review, pk=review_id)
        return render(request, 'reviews/delete.template.html', {
            "review": review_to_delete
        })
