import datetime
from django.db import models
from django.utils import timezone


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    review = models.TextField(max_length=1000)
    image = models.ImageField(upload_to=f'images/{datetime.datetime.now()}__')
    date_created = models.DateTimeField(default=timezone.now)
    date_modified =  models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'feedback'
