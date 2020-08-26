# accounts/urls.py
from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    url(r"^signup/$", views.signup, name="signup"),
    url(r"^update/$", views.update_profile, name="update"),
    url(r"^profile/$", TemplateView.as_view(template_name="accounts/profile.html")),
    url(r"^profile/edit$", TemplateView.as_view(template_name="accounts/profile_edit.html")),

]