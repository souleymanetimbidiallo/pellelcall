from django.urls import path, re_path
from django.conf.urls import url, include
from django.views.generic import TemplateView, ListView, CreateView
from . import views

urlpatterns = [
    url(r"^$", views.home, name="home"),
    url(r"^offers/$", views.OfferList.as_view(), name="offer_list"),
    url(r"^offer/(?P<pk>\d+)$", views.OfferDetailView.as_view(), name="offer_detail"),
    url(r"^create/$", views.conferenceCreate, name="conference"),
    url(r"^join/$", views.TemplateView.as_view(template_name="meeting/meeting_join.html")),
]
