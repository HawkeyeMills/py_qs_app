from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.metrics_list, name='metrics_list'),
]