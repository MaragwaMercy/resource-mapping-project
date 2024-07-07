from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import *

class WardsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Wards
        geo_field = 'geom'
        fields = '__all__'

class HospitalsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Hospitals
        geo_field = 'geom'
        fields = '__all__'

class SchoolsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Schools
        geo_field = 'geom'
        fields = '__all__'

class RiversSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Rivers
        geo_field = 'geom'
        fields = '__all__'

class ForestsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Forests
        geo_field = 'geom'
        fields = '__all__'

class RoadsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Roads
        geo_field = 'geom'
        fields = '__all__'

class SubcountySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Subcounty
        geo_field = 'geom'
        fields = '__all__'

class TownsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Towns
        geo_field = 'geom'
        fields = '__all__'

class WaterBodiesSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = WaterBodies
        geo_field = 'geom'
        fields = '__all__'

class PublicLandSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = PublicLand
        geo_field = 'geom'
        fields = '__all__'
