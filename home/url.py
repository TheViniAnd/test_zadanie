from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^list/$', views.pub_det, name='home_list')
    ]