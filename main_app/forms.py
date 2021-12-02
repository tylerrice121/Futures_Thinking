from django import forms
from .models import UserEntries, Profile, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = UserEntries
        fields = [
            'in_the_future',
            'title_of_that_future',
            'tags',
            'relevant_link',
            'optional_image',
            'optional_video',
            
        ]


class ProfileForm(forms.ModelForm):
  class Meta:
        model = Profile
        fields = [
            'bio',
        ]

class CommentsForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = [
        'name',
        'body',
    ]


class SignUpForm(UserCreationForm):
  email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2', )