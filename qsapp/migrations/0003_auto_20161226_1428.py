# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 20:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('qsapp', '0002_auto_20161221_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetricType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metrictype', models.CharField(blank=True, max_length=255)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='metric',
            name='metric_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='metricconfig',
            name='fitbitvalue',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='metricconfig',
            name='metrictype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qsapp.MetricType'),
        ),
    ]
