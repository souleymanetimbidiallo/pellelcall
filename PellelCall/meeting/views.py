from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    """ Vue qui affiche la page d'accueil des conférences"""

    return render(request, 'meeting/home.html', locals())
