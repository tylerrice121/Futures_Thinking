from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class UserEntries(models.Model):
    title = models.CharField(max_length=100)
    entry = models.CharField(max_length=350)
    img = models.CharField(max_length=250)
    video_url = models.CharField(max_length=250)
    date = models.DateField('Post Date')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} was created on {self.date} with the id of {self.id}"

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
    

class AllEntries(models.Model):
    user_entries = models.ForeignKey(UserEntries, on_delete=models.CASCADE)

    def __str__(self):
        return f"This user entry is from {self.user_entries}"