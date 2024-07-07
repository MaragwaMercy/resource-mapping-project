from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'wards', WardsViewSet)
router.register(r'hospitals', HospitalsViewSet)
router.register(r'schools', SchoolsViewSet)
router.register(r'rivers', RiversViewSet)
router.register(r'forests', ForestsViewSet)
router.register(r'roads', RoadsViewSet)
router.register(r'subcounty', SubcountyViewSet)
router.register(r'towns', TownsViewSet)
router.register(r'waterbodies', WaterBodiesViewSet)
router.register(r'publicland', PublicLandViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('home/', HomepageView.as_view(), name='home'),
    path('', include(router.urls)),
]
