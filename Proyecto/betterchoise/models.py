from django.db import models

# Create your models here.

class Search(models.Model):
    brand =  models.TextField(max_length=100, blank=True, default='')
    model = models.TextField(max_length=100, blank=True, default='')
    price = models.TextField(max_length=100, blank=True, default='')
    page = models.TextField(max_length=100, blank=True, default='')
    use = models.TextField(max_length=100, blank=True, default='')
    category = models.TextField(max_length=100, blank=True, default='')
    img = models.TextField(max_length=100, blank=True, default='')
    