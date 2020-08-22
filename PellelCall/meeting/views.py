from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from meeting.models import Offer, User, Profile, Souscription, Conference

# Create your views here.

def home(request):
    """ Vue qui affiche la page d'accueil des conférences"""
    return render(request, 'meeting/home.html', locals())

class OfferList(ListView):
    model = Offer
    context_object_name = 'offers'
    template_name = 'meeting/offers.html'

class OfferDetailView(DetailView):
    model = Offer
    context_object_name = 'offer'
    template_name='meeting/offer_detail.html'