# Generated by Django 4.1 on 2022-09-25 13:40

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cycletourmap", "0003_remove_activity_start_latitude_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="activity",
            name="end_latlng",
            field=django.contrib.gis.db.models.fields.PointField(
                blank=True, null=True, srid=4326
            ),
        ),
    ]
