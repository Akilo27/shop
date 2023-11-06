from django.urls import re_path as url
from . import views


app_name = 'orders'

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
]