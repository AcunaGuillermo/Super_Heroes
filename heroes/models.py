from django.db import models

# Create your models here.
class superHeroe(models.Model):
    nombre = models.CharField(max_length=128)
    fecha_nacimiento = models.DateField()
    peso_kg = models.IntegerField()
    

class Poder(models.models):
    nombre = models.CharField(max_length=128)
    super_heroes = models.ForeignKey('superHeroes',on_delete=models.CASCADE)
    