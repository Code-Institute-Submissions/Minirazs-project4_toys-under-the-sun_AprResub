from django.shortcuts import render, get_object_or_404, reverse, HttpResponse
from toy.models import Toy

import stripe
import json
from django.conf import settings
from django.contrib.sites.models import Site
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
