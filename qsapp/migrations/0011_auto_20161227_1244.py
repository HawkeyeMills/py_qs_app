# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 18:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('qsapp', '0010_auto_20161227_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailygrade',
            name='grade_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
