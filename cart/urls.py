from django.urls import path, include
import cart.views

urlpatterns = [
    path('', cart.views.index,
         name='show_cart_route')
]
