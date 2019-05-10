from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices
# Create your views here.

from realtors.models import Realtor
from listings.models import Listing

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
    'listings':listings,
    'state_choices':state_choices,
    'bedroom_choices':bedroom_choices,
    'price_choices':price_choices
    }
    return render(request,'pages/index.html',context)

def about(request):
    realtors = Realtor.objects.all()
    context = {
    'realtors':realtors
    }
    return render(request,'pages/about.html', context)

def listing(request):
    return render(request, 'listings/listing.html')

def registration(request):
    return render(request, 'pages/registration.html')

def login(request):
    return render(request, 'pages/login.html')
