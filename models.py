# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class Wards(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    geom = models.MultiPolygonField(srid=32737, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wards'


class Rivers(models.Model):
    gid = models.AutoField(primary_key=True)
    layer = models.CharField(max_length=17, blank=True, null=True)
    dgc_codice = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    code = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    geom = models.MultiLineStringField(srid=32737, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rivers'


class Forests(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    geom = models.MultiPolygonField(srid=32737, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forests'


class Roads(models.Model):
    gid = models.AutoField(primary_key=True)
    layer = models.CharField(max_length=17, blank=True, null=True)
    old_rid = models.CharField(max_length=40, blank=True, null=True)
    length = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    roadclass = models.CharField(max_length=1, blank=True, null=True)
    roadnum = models.CharField(max_length=20, blank=True, null=True)
    geom = models.MultiLineStringField(srid=32737, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roads'


class Subcounty(models.Model):
    gid = models.AutoField(primary_key=True)
    gm_type = models.CharField(max_length=17, blank=True, null=True)
    const_no = models.IntegerField(blank=True, null=True)
    const_nam = models.CharField(max_length=9, blank=True, null=True)
    county_nam = models.CharField(max_length=4, blank=True, null=True)
    subcounty = models.CharField(max_length=50, blank=True, null=True)
    geom = models.MultiPolygonField(srid=32737, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subcounty'


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
    geom = models.PointField(srid=32737, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'towns'


class WaterBodies(models.Model):
    gid = models.AutoField(primary_key=True)
    layer = models.CharField(max_length=17, blank=True, null=True)
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
    geom = models.MultiPolygonField(srid=32737, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'water_bodies'
