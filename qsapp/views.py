from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import render, render_to_response, get_object_or_404

from django.http import HttpResponseRedirect
from django.views.generic import CreateView

from django.utils import timezone

from datetime import date

from .models import Metric, MetricConfig, DailyGrade

from .forms import MetricForm

def metrics_list(request):
    metrics = Metric.objects.filter(metric_date=date.today()).order_by('metric_config__orderby')
    #.order_by('-metric_date')
    return render(request, 'qsapp/metrics_list.html', {'metrics': metrics})

def metric_detail(request, pk):
    metric = get_object_or_404(Metric, pk=pk)
    return render(request, 'qsapp/metric_detail.html', {'metric': metric})

def metric_new(request):
    print(request.method)
    if request.method == "POST":
        form = MetricForm(request.POST)
        if form.is_valid():
            metric = form.save(commit=False)
            #metric.created_date = timezone.now
            #metric.updated_date = timezone.now
            metric.save()
            return redirect('metric_detail', pk=metric.pk)
    else:
        form = MetricForm()
    return render(request, 'qsapp/metric_edit.html', {'form': form})

def metric_edit(request, pk):
    metric = get_object_or_404(Metric, pk=pk)
    if request.method == "POST":
        form = MetricForm(request.POST, instance=metric)
        if form.is_valid():
            metric = form.save(commit=False)
            #metric.updated_date = timezone.now
            metric.save()
            return redirect('metric_detail', pk=metric.pk)
    else:
        form = MetricForm(instance=metric)
    return render(request, 'qsapp/metric_edit.html', {'form': form})