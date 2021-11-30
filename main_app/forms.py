from django import forms
from .models import UserEntries

class PostForm(forms.ModelForm):
    class Meta:
        model = UserEntries
        fields = [
            'title',
            'entry',
            'tags',
            'video',
        ]

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
  email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')