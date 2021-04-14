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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # homepage
    path('', toy.views.redirect_view, name='home'),
    # toy urls
    path('toy/', include('toy.urls')),

    # review urls
    path('review/', include('review.urls')),

    # order urls
    path('order/', include('order.urls')),

    # cart urls
    path('cart/', include('cart.urls')),

    # checkout urls
    path('checkout/', include('checkout.urls'))
]
