from .forms import SignUpForm, CommentForm
from django.db.models.fields import SlugField
from django.shortcuts import render
from .models import Comment, UserEntries, Profile
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from taggit.models import Tag




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
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            # this creates a session entry in the database
            login(request, user)
            # # and it persists that session sitewide until the user logs out
            return redirect('profile')
        else:
            error_message = 'invalid data - please try again'
    # this is for GET requests, assuming our user clicked on "signup" from the navbar
    form = SignUpForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)



class TagIndexView(ListView):
    # queryset = UserEntries.objects.all()
    model = UserEntries
    template_name = 'feed.html'

    # context_object_name = 'posts'
   
    def get_queryset(self):
       return UserEntries.objects.filter(tags__slug=self.kwargs.get('tags_slug'))

class TagMixin(object):
    def get_context_data(self, **kwargs):
        context =super(TagMixin,self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

class Feed(TagMixin, ListView):
    queryset = UserEntries.objects.order_by('-date')
    model = UserEntries
    template_name = 'feed.html'


class AddProfile(LoginRequiredMixin, ListView):
    model = Profile
    fields = '__all__'
    template_name = 'main_app/profile_form.html'

    def form_valid(self, form):
        form.instance.profile = self.request.profile
        return super().form_valid(form)

class Profile(LoginRequiredMixin, ListView):
    model = UserEntries
    template_name = 'profile/index.html'
    def get_queryset(self):
        queryset = UserEntries.objects.filter(user=self.request.user)
        queryset = UserEntries.objects.order_by('-date')
        return queryset

class EntryCreate(LoginRequiredMixin, CreateView):
    model = UserEntries
    fields = ('in_the_future', 'title_of_that_future', 'relevant_link','tags','optional_image', 'optional_video' )

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddCommentView(CreateView):
    model = Comment
    template_name = 'profile/add_comment.html'
    form_class = CommentForm
    #fields = ('entry', 'name', 'body')
  
    
    def form_valid(self, form):
        form.instance.entry_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = 'detail.html'
   

class EntryUpdate(LoginRequiredMixin, UpdateView):
  model = UserEntries
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['in_the_future', 'title_of_that_future',   'relevant_link', 'tags','optional_image', 'optional_video' ]

class EntryDelete(LoginRequiredMixin, DeleteView):
    model = UserEntries
    success_url = '/profile/'

    def get_queryset(self):
        queryset = UserEntries.objects.filter(user=self.request.user)
        return queryset
  
