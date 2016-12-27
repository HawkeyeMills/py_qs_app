from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import render, render_to_response, get_object_or_404

from django.http import HttpResponseRedirect

from django.utils import timezone

from .models import Metric, MetricConfig
from .models import DailyGrade

from .forms import MetricForm

def metrics_list(request):
    metrics = Metric.objects.filter(metric_date__lte=timezone.now()).order_by('metric_date')
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
            #metric.metric_config = request.metric_config
            metric.save()
            return redirect('metric_detail', pk=metric.pk)
    else:
        form = MetricForm()
    return render(request, 'qsapp/metric_edit.html', {'form': form})

def metric_edit(request, pk):
    metric = get_object_or_404(Metric, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            metric = form.save(commit=False)
            metric.metric_date = request.metric
            #post.published_date = timezone.now()
            metric.save()
            return redirect('metric_detail', pk=metric.pk)
    else:
        form = MetricForm(instance=metric)
    return render(request, 'qsapp/metric_edit.html', {'form': form})