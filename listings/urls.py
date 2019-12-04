from . import views
from django.urls import path
urlpatterns = [
    path('', views.index, name='listings'),
    path('<listing_id>', views.listing, name='listing'),
    path('search/', views.search, name='search'),
]
