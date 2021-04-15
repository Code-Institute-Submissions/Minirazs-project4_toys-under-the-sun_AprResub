from django.urls import path
import order.views

urlpatterns = [
    path('', order.views.index,
         name='show_order_route')

]
