from django.db import models
from datetime import datetime


class Locations(models.Model):
    place = models.CharField(max_length=100)
    timing = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images')
    category = models.CharField(max_length=50)
    created = models.DateTimeField(default=datetime.now())
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.place

    class Meta:
        db_table = 'locations'
        ordering = ('category',)
