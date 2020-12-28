from django.db import models

# Create your models here.

class Menus(models.Model):
    entrada = models.CharField(max_length=40)
    fondo = models.CharField(max_length=40)
    postre = models.CharField(max_length=40)
    precio = models.FloatField()