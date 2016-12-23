from django.shortcuts import render
from django.utils import timezone
from .models import Metric
from .models import DailyGrade

def metrics_list(request):
    metrics = Metric.objects.filter(metric_date__lte=timezone.now()).order_by('metric_date')
    return render(request, 'qsapp/metrics_list.html', {'metrics': metrics})