from rest_framework import serializers
from listings.models import Listing

# serializer convert model into JSON
from realtors.models import Realtor


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('realtor', 'title', 'address', 'city', 'price', 'bathrooms', 'bedrooms', 'garage', 'sqft', 'lot_size',
                  'photo_main')


class RealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realtor
        fields = (
            'name', 'photo', 'description', 'email', 'phone'
        )


'''
1. pip install djangorestframework
2. set rest_framework in INSTALLED_APPS
3. include model name and fields to be converted into JSON format
'''
