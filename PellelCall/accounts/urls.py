# accounts/urls.py
from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'), 
    url(r"^profile/$", TemplateView.as_view(template_name="accounts/profile.html")),

]