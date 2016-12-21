# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 22:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qsapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DailyGrades',
            new_name='DailyGrade',
        ),
        migrations.RenameModel(
            old_name='Grades',
            new_name='Grade',
        ),
        migrations.RenameModel(
            old_name='GradeCalcs',
            new_name='GradeCalc',
        ),
        migrations.RenameModel(
            old_name='GradeConfigs',
            new_name='GradeConfig',
        ),
        migrations.RenameModel(
            old_name='Metrics',
            new_name='Metric',
        ),
        migrations.RenameModel(
            old_name='MetricConfigs',
            new_name='MetricConfig',
        ),
        migrations.RenameModel(
            old_name='MetricGrades',
            new_name='MetricGrade',
        ),
        migrations.RenameModel(
            old_name='Notes',
            new_name='Note',
        ),
    ]