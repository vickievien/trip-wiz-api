from pyexpat import model
from django.db import models

# Create your models here.
class Review(models.Model):
    reviewer_name = models.CharField(max_length=32)
    city = models.CharField(max_length=32, blank=False)
    country = models.CharField(max_length=32, blank=False)
    trip_start_date = models.DateField(default='2022-01-01')
    trip_end_date = models.DateField(default='2022-01-05')
    review = models.TextField()
    img = models.CharField(default='https://i.imgur.com/99v0yRs.jpg', max_length=100)
    test = models.CharField(max_length=32)