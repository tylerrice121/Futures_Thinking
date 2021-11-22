from django.db import models


class UserEntries(models.Model):
    title = models.CharField(max_length=100)
    entry = models.CharField(max_length=350)
    img = models.CharField(max_length=250)
    video_url = models.CharField(max_length=250)
    date = models.DateField('Post Date')

    def __str__(self):
        return f"{self.title} was created on {self.date} with the id of {self.id}"

    