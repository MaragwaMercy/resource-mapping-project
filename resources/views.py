from rest_framework import viewsets
from django.views.generic import TemplateView
from rest_framework_gis.filters import DistanceToPointFilter
from django.contrib.gis.geos import *
from django.contrib.gis.db.models.functions import *
from .models import *
from .serializers import *

class HomepageView(TemplateView):
    template_name = 'front.html'

class WardsViewSet(viewsets.ModelViewSet):
    queryset = Wards.objects.all()
    serializer_class = WardsSerializer
    # Enable filtering based on distance to a point
    filter_backends = [DistanceToPointFilter]
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class HospitalsViewSet(viewsets.ModelViewSet):
    queryset = Hospitals.objects.all()
    serializer_class = HospitalsSerializer
    filter_backends = [DistanceToPointFilter]
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True



    
class SchoolsViewSet(viewsets.ModelViewSet):
    queryset = Schools.objects.all()
    serializer_class = SchoolsSerializer
    # Enable filtering based on distance to a point
    filter_backends = [DistanceToPointFilter]
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class RiversViewSet(viewsets.ModelViewSet):
    queryset = Rivers.objects.all()
    serializer_class = RiversSerializer
    # Enable filtering based on distance to a point
    filter_backends = [DistanceToPointFilter]
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class ForestsViewSet(viewsets.ModelViewSet):
    queryset = Forests.objects.all()
    serializer_class = ForestsSerializer
    # Enable filtering based on distance to a point
    filter_backends = [DistanceToPointFilter]
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class RoadsViewSet(viewsets.ModelViewSet):
    queryset = Roads.objects.all()
    serializer_class = RoadsSerializer
    # Enable filtering based on distance to a point
    filter_backends = [DistanceToPointFilter]
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class SubcountyViewSet(viewsets.ModelViewSet):
    queryset = Subcounty.objects.all()
    serializer_class = SubcountySerializer
    # Enable filtering based on distance to a point
    filter_backends = [DistanceToPointFilter]
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class TownsViewSet(viewsets.ModelViewSet):
    queryset = Towns.objects.all()
    serializer_class = TownsSerializer
    filter_backends = [DistanceToPointFilter]
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class WaterBodiesViewSet(viewsets.ModelViewSet):
    queryset = WaterBodies.objects.all()
    serializer_class = WaterBodiesSerializer
    filter_backends = [DistanceToPointFilter]
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True

class PublicLandViewSet(viewsets.ModelViewSet):
    queryset = PublicLand.objects.all()
    serializer_class = PublicLandSerializer
    filter_backends = [DistanceToPointFilter]
    distance_filter_field = 'geom'
    bbox_filter_include_overlapping = True
