from django.urls import path, include
import review.views

urlpatterns = [
    path('', review.views.index,
         name='show_review_route'),
    path('create/<toy_id>', review.views.create_review,
         name='create_review_route'),
    path('update/<review_id>', review.views.update_review,
         name='update_review_route'),
    path('delete/<review_id>', review.views.delete_review,
         name='delete_review_route')
]
