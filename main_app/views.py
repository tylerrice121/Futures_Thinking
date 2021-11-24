from django.shortcuts import render
from .models import UserEntries, AllEntries
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.

def home(request):
    return render(request, 'home.html')

def detail(request, pk):
    entry = UserEntries.objects.get(id=pk)
    return render(request, 'profile/detail.html',{
        'entry': entry
    })

class Feed(ListView):
    model = UserEntries
    template_name = 'feed.html'

class Profile(ListView):
    model = UserEntries
    template_name = 'profile/index.html'

class EntryCreate(CreateView):
    model = UserEntries
    fields = ('title', 'entry', 'img', 'video_url', 'date')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
