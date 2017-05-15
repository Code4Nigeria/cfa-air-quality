# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-08 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfaairquality', '0006_auto_20170503_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensordetails',
            name='sensor_data_offset',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sensordetails',
            name='sensor_offset_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
