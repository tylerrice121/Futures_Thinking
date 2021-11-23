from django.shortcuts import render
from .models import UserEntries, AllEntries
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.

def home(request):
    return render(request, 'home.html')

def detail(request, pk):
    entry = UserEntries.objects.get(id=pk)
    return render(request, 'profile/detail.html')

class Feed(ListView):
    model = UserEntries
    template_name = 'feed.html'

class Profile(ListView):
    model = UserEntries
    template_name = 'profile/index.html'

class EntryCreate(CreateView):
    model = UserEntries
    fields = '__all__'
