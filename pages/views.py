from django.shortcuts import render

# Create your views here.

from listings.models import Listing


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    context = {
        'listings': listings,
        'title': 'E-Commerce'
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')

