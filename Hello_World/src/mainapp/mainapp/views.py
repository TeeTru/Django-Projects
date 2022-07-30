from django.http import HttpResponse
from django.shortcuts import render




def home(request):
    profiles = ['Profile', '.objects', '.all']
    return render(request, "home.html", {'profiles': profiles})
