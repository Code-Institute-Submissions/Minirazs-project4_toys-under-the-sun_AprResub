from django.urls import path, include
import cart.views

urlpatterns = [
    path('', cart.views.index,
         name='show_cart_route'),
    path('add/<toy_id>', cart.views.add_to_cart,
         name='add_to_cart_route'),
]
