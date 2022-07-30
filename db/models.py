from django.db import models
from django.contrib.auth import models as auth_models

'''
documentation: https://docs.djangoproject.com/en/4.0/ref/models/fields/
'''


class Products(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=False)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    price = models.FloatField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    presence = models.BooleanField(default=False)
    author = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)

