from django.urls import path, include
import toy.views

urlpatterns = [
    path('', toy.views.index,
         name='show_toy_route'),
    path('create', toy.views.create_toy,
         name='create_toy_route'),
    path('update/<toy_id>', toy.views.update_toy,
         name='update_toy_route'),
    path('delete/<toy_id>', toy.views.delete_toy,
         name='delete_toy_route'),
    path('<toy_id>', toy.views.one_toy,
         name='one_toy_route'),
    path('search/', toy.views.search)
]