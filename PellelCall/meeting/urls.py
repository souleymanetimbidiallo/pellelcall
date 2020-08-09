from django.urls import path, re_path
from django.conf.urls import url, include
from django.views.generic import TemplateView, ListView, CreateView
from . import views

urlpatterns = [
    url(r"^$", views.home, name="home"),
]
