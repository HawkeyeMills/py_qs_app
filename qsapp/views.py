from django.shortcuts import render

def metrics_list(request):
    return render(request, 'qsapp/metrics_list.html', {})