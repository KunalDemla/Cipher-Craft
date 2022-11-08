from django.db import models
from django.contrib.auth.models import User

class Ciphers(models.Model):
    name=models.CharField(max_length=250)
    title = models.CharField(max_length=250,blank=True)
    favourites = models.ManyToManyField(User,related_name='favourite',default=None,blank=True)
    
    def __str__(self):
        return f'{self.name}'