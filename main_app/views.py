from django.shortcuts import render
from .models import UserEntries, AllEntries
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def home(request):
    return render(request, 'home.html')

def detail(request, pk):
    entry = UserEntries.objects.get(id=pk)
    return render(request, 'profile/detail.html',{
        'entry': entry
    })

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # handle the creation of a new user
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # this creates a session entry in the database
            login(request, user)
            # # and it persists that session sitewide until the user logs out
            return redirect('feed')
        else:
            error_message = 'invalid data - please try again'
    # this is for GET requests, assuming our user clicked on "signup" from the navbar
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

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
