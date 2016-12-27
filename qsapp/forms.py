from django import forms

from .models import Metric

class MetricForm(forms.ModelForm):

    class Meta:
        model = Metric
        fields = ('metric_config', 'metric_date', 'value',)