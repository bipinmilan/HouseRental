from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Listing


# Create your views here.


def index(request):
    '''listings = Listing.objects.all() #return all data from table

    context = {
        'listings': listings
    }
    return render(request, 'listings/listings.html', context)'''

    # - denotes descending order

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 2)  # return number of items in one page
    page = request.GET.get('page')  # request page
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


# when view function returns a web page as a HttpResponse rather than a simple string then we use render
# render pass data dictionary to the template easily

'''def list(request,id):
    listing = Listing.objects.get(id=id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)'''


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # keywords

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__iexact=bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price_lte=price)

    context = {
        'listings': queryset_list,
    }

    return render(request, 'search/search.html', context)


# Class based View
'''class ListingView(ListView):
    template_name = "listings/listing.html"
    queryset = Listing.objects.all()
    context_object_name = "bipin"'''
