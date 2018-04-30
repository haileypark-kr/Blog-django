from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.exp_list, name='exp_list'),
]