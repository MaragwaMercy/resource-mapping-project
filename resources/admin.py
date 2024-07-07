from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import *


    
admin.site.register(Wards, LeafletGeoAdmin)
admin.site.register(Hospitals, LeafletGeoAdmin)
admin.site.register(Schools, LeafletGeoAdmin)
admin.site.register(Rivers, LeafletGeoAdmin)
admin.site.register(Forests, LeafletGeoAdmin)
admin.site.register(Roads, LeafletGeoAdmin)
admin.site.register(Subcounty, LeafletGeoAdmin)
admin.site.register(Towns, LeafletGeoAdmin)
admin.site.register(WaterBodies, LeafletGeoAdmin)
admin.site.register(PublicLand, LeafletGeoAdmin)

