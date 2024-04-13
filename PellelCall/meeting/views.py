from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required

from .models import Offer, User, Profile, Souscription, Conference
from .forms import ConferenceForm

# Create your views here.

def home(request):
    """ Vue qui affiche la page d'accueil des conférences"""
    return render(request, 'meeting/home.html', locals())

@login_required
def conferenceCreate(request):
    if request.method == 'POST':
        form = ConferenceForm(request.POST)
        if form.is_valid():
            conference = form.save(commit=False)
            conference.initiator = request.user
            conference.save()
            return redirect('conference')
    else:
        form = ConferenceForm()
        
    return render(request, 'meeting/meeting_create.html', {'form': form})
    

class OfferList(ListView):
    model = Offer
    context_object_name = 'offers'
    template_name = 'meeting/offers.html'

class OfferDetailView(DetailView):
    model = Offer
    context_object_name = 'offer'
    template_name='meeting/offer_detail.html'


class ConferenceView(CreateView):
    form_class = ConferenceForm
    template_name = 'meeting/meeting_create.html'
    success_url = 'conference'
