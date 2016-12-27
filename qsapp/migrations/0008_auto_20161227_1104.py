# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 17:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qsapp', '0007_auto_20161226_1532'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dailygrade',
            old_name='grade_id',
            new_name='grade',
        ),
        migrations.RenameField(
            model_name='gradeconfig',
            old_name='grade_calc_id',
            new_name='grade_calc',
        ),
        migrations.RenameField(
            model_name='gradeconfig',
            old_name='metric_config_id',
            new_name='metric_config',
        ),
        migrations.RenameField(
            model_name='metric',
            old_name='metric_config_id',
            new_name='metric_config',
        ),
        migrations.RenameField(
            model_name='metricconfig',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='metricgrade',
            old_name='grade_id',
            new_name='grade',
        ),
        migrations.RenameField(
            model_name='metricgrade',
            old_name='metric_id',
            new_name='metric',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='user_id',
            new_name='user',
        ),
    ]
