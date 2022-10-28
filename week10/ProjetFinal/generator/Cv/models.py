from django.db import models
from django import forms

 # Create your models here.
from django.db import models



 # Create your models here.
class Profile(models.Model):
    image = models.ImageField(upload_to='upload/', blank=True)
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    competance = models.CharField(max_length=1000)
    langue = models.CharField(max_length=500)
    interet = models.CharField(max_length=500)
    qualite=models.CharField(max_length=500)
    profile=models.TextField()
    experience = models.TextField()
    education = models.TextField()
    Projet = models.TextField()

    date_added = models.DateTimeField(auto_now=True)
    actif= models.BooleanField(default=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_added']





