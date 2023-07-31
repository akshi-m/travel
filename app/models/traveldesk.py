from django.db import models
from django.utils import timezone


class Traveldesk(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    expected_date = models.DateField()
    phone = models.CharField(max_length=10)
    message = models.TextField(max_length=1000)
    number_of_person = models.IntegerField(default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'traveldesk'
