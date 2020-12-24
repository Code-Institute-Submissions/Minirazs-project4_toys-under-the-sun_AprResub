from django.urls import path, include
import cart.views

urlpatterns = [
    path('add/<toy_id>', cart.views.add_to_cart,
         name='add_to_cart_route'),
    path('view_cart', cart.views.view_cart,
         name='view_cart_route')
]
