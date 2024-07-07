# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class PublicLand(models.Model):
    gid = models.AutoField(primary_key=True)
    l_r_no = models.CharField(max_length=43, blank=True, null=True)
    institution = models.CharField(max_length=146, blank=True, null=True)
    situation = models.CharField(max_length=84, blank=True, null=True)
    acreage_acres = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=211, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'public_land'
