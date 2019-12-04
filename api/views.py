from rest_framework import viewsets, permissions

from listings.models import Listing
from realtors.models import Realtor
from .serializers import ListingSerializer, RealtorSerializer


class ListingView(viewsets.ModelViewSet):
    # get ListingObjects in queryset
    queryset = Listing.objects.all()
    # serializing the ListingSerializer class here
    serializer_class = ListingSerializer

    # permission_classes = (permissions.IsAdminUser,)


class RealtorView(viewsets.ModelViewSet):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer
