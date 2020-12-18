from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def index(request):
    return render(request, 'reviews/index.template.html')
