# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qsapp', '0009_metricconfig_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metric',
            name='value',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
