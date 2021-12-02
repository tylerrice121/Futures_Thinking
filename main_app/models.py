from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import NullBooleanField
from django.urls import reverse
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
from taggit.managers import TaggableManager


class UserEntries(models.Model):
 
    in_the_future = models.TextField() 
    title_of_that_future = models.CharField(max_length=350)
    relevant_link = models.URLField(max_length=350)
    tags = TaggableManager()
    # slug = models.SlugField(unique=True, max_length=100)
    optional_image = models.CharField(max_length=250, blank=True)
    optional_video = EmbedVideoField(blank=True)
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_of_that_future
        # return f"{self.title} was created on {self.date} with the id of {self.id}"

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.id})
    

class Comment(models.Model):
    entry = models.ForeignKey(UserEntries, related_name='comments', on_delete= models.CASCADE)
    name = models.CharField(max_length=250, blank=True)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.entry.title_of_that_future, self.name)

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=CASCADE)
    bio = models.TextField()

    def __str__(self):
        return str(self.user)

class AllEntries(models.Model):
    user_entries = models.ForeignKey(UserEntries, on_delete=models.CASCADE)

    def __str__(self):
        return f"This user entry is from {self.user_entries}"

# set email for login
USERNAME_FIELD = 'email'
REQUIRED_FIELDS = ['username']

