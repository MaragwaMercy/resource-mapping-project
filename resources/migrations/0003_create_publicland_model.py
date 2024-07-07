from django.db import migrations, models
import django.contrib.gis.db.models.fields

class Migration(migrations.Migration):

    dependencies = [
        ("resources", "0002_auto_20240606_1334"),  
    ]

    operations = [
        migrations.CreateModel(
            name='PublicLand',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('l_r_no', models.CharField(max_length=50, blank=True, null=True)),
                ('institution', models.CharField(max_length=150, blank=True, null=True)),
                ('situation', models.CharField(max_length=100, blank=True, null=True)),
                ('acreage_acres', models.FloatField(blank=True, null=True)),
                ('status', models.CharField(max_length=250, blank=True, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326, blank=True, null=True)),
            ],
            options={
                'db_table': 'public_land',
                'managed': True,
                'verbose_name_plural': 'public_land',
            },
        ),
    ]
