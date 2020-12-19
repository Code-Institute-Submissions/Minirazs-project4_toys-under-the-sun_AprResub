"""ToysProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import toy.views
import reviews.views
import orders.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # toy urls
    path('toys/', toy.views.index,
         name='show_toy_route'),
    path('toys/create', toy.views.create_toy,
         name='create_toy_route'),
    path('toys/update/<toy_id>', toy.views.update_toy,
         name='update_toy_route'),
    path('toys/delete/<toy_id>', toy.views.delete_toy,
         name='delete_toy_route'),
    # review urls
    path('reviews/', reviews.views.index,
         name='show_review_route'),
    path('reviews/create/<toy_id>', reviews.views.create_review,
         name='create_review_route'),
    path('reviews/update/<review_id>', reviews.views.update_review,
         name='update_review_route'),
    path('reviews/delete/<review_id>', reviews.views.delete_review,
         name='delete_review_route'),
    # order urls
    path('orders/', orders.views.index,
         name='show_order_route')
]
