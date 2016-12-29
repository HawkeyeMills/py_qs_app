from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django.contrib.admin import widgets
from django.forms.formsets import formset_factory

from .models import Metric, MetricConfig, GradeConfig

class MetricForm(forms.ModelForm):
    class Meta:
        model = Metric
        fields = ['metric_config', 'metric_date', 'value']
        metric_date = forms.DateField()
        exclude = ()