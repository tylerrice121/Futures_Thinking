from django.shortcuts import render
from .models import UserEntries, AllEntries
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.

def home(request):
    return render(request, 'home.html')

def feed(request):
    return render(request, 'feed.html')

class Profile(ListView):
    model = UserEntries
    template_name = 'profile/index.html'
