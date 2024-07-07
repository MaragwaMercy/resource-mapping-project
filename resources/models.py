from django.db import models
from django.contrib.gis.db import models


class Wards(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    geom = models.MultiPolygonField(srid=4326, blank=True, null=True)

    def __str__(self):
        return str(self.name)
    class Meta:
        managed = False
        db_table = 'wards'
        verbose_name_plural = 'wards'
        


class Hospitals(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    keph_level = models.CharField(max_length=100, blank=True, null=True)
    facility_type = models.CharField(max_length=100, blank=True, null=True)
    facility_category = models.CharField(max_length=100, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True, srid=4326)

    def __str__(self):
        return str(self.name)
    class Meta:
        managed = False
        db_table = 'hospitals'
        verbose_name_plural = 'hospitals'


class Schools(models.Model):
    gid = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=100, blank=True, null=True)
    level = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    zone = models.CharField(max_length=100, blank=True, null=True)
    ward = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    sub_county = models.CharField(max_length=100, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True, srid=4326)

    def __str__(self):
        return str(self.school_name)
    class Meta:
        managed = False
        db_table = 'schools'
        verbose_name_plural = 'schools'

class Rivers(models.Model):
    gid = models.AutoField(primary_key=True)
    layer = models.CharField(max_length=17, blank=True, null=True)
    dgc_codice = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    code = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    geom = models.MultiLineStringField(srid=4326, blank=True, null=True)

    def __str__(self):
        return str(self.name)
    class Meta:
        managed = False
        db_table = 'rivers'
        verbose_name_plural = 'rivers'


class Forests(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    geom = models.MultiPolygonField(srid=4326, blank=True, null=True)

    def __str__(self):
        return str(self.name)
    class Meta:
        managed = False
        db_table = 'forests'
        verbose_name_plural = 'forests'


class Roads(models.Model):
    gid = models.AutoField(primary_key=True)
    layer = models.CharField(max_length=20, blank=True, null=True)
    old_rid = models.CharField(max_length=40, blank=True, null=True)
    length = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    roadclass = models.CharField(max_length=5, blank=True, null=True)
    roadnum = models.CharField(max_length=20, blank=True, null=True)
    geom = models.MultiLineStringField(srid=4326, blank=True, null=True)

    def __str__(self):
        return str(self.roadclass)
    class Meta:
        managed = False
        db_table = 'roads'
        verbose_name_plural = 'roads'


class Subcounty(models.Model):
    gid = models.AutoField(primary_key=True)
    gm_type = models.CharField(max_length=17, blank=True, null=True)
    const_no = models.IntegerField(blank=True, null=True)
    const_nam = models.CharField(max_length=9, blank=True, null=True)
    county_nam = models.CharField(max_length=4, blank=True, null=True)
    subcounty = models.CharField(max_length=50, blank=True, null=True)
    geom = models.MultiPolygonField(srid=4326, blank=True, null=True)

    def __str__(self):
        return str(self.subcounty)
    class Meta:
        managed = False
        db_table = 'subcounty'
        verbose_name_plural = 'subcounties'


class Towns(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    layer = models.CharField(max_length=21, blank=True, null=True)
    tname = models.CharField(max_length=30, blank=True, null=True)
    admstatus = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    dont_label = models.CharField(max_length=5, blank=True, null=True)
    source = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    labels = models.CharField(max_length=30, blank=True, null=True)
    new_status = models.CharField(max_length=25, blank=True, null=True)
    origstatus = models.CharField(max_length=20, blank=True, null=True)
    geom = models.PointField(srid=4326, blank=True, null=True)

    def __str__(self):
        return str(self.name)
    class Meta:
        managed = False
        db_table = 'towns'
        verbose_name_plural = 'towns'


class WaterBodies(models.Model):
    gid = models.AutoField(primary_key=True)
    layer = models.CharField(max_length=20, blank=True, null=True)
    id = models.FloatField(blank=True, null=True)
    osm_id = models.CharField(max_length=20, blank=True, null=True)
    z_order = models.FloatField(blank=True, null=True)
    natural = models.CharField(max_length=80, blank=True, null=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    name_en = models.CharField(max_length=80, blank=True, null=True)
    type = models.CharField(max_length=80, blank=True, null=True)
    ele = models.CharField(max_length=80, blank=True, null=True)
    water = models.CharField(max_length=80, blank=True, null=True)
    wetland = models.CharField(max_length=80, blank=True, null=True)
    wood = models.CharField(max_length=80, blank=True, null=True)
    geom = models.MultiPolygonField(srid=4326, blank=True, null=True)

    def __str__(self):
        return str(self.name)
    class Meta:
        managed = False
        db_table = 'water_bodies'
        verbose_name_plural = 'water_bodies'

class PublicLand(models.Model):
    gid = models.AutoField(primary_key=True)
    l_r_no = models.CharField(max_length=50, blank=True, null=True)
    institution = models.CharField(max_length=150, blank=True, null=True)
    situation = models.CharField(max_length=100, blank=True, null=True)
    acreage_acres = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=250, blank=True, null=True)
    current_status = models.CharField(max_length=50, blank=True, null=True)
    geom = models.PointField(srid=4326, blank=True, null=True)

    def __str__(self):
        return str(self.institution)
    class Meta:
        managed = False
        db_table = 'public_land'
        verbose_name_plural = 'public land'


