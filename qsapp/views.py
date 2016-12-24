from django.shortcuts import render
from django.utils import timezone

from .models import Metric
from .models import DailyGrade

from django.shortcuts import render, get_object_or_404

def metrics_list(request):
    metrics = Metric.objects.filter(metric_date__lte=timezone.now()).order_by('metric_date')
    return render(request, 'qsapp/metrics_list.html', {'metrics': metrics})

def metric_detail(request, pk):
    metric = get_object_or_404(Metric, pk=pk)
    return render(request, 'qsapp/metric_detail.html', {'metric': metric})