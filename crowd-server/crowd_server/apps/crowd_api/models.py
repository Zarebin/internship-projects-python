from django.db import models


class Species(models.Model):
   name = models.CharField(max_length=100)
   classification = models.CharField(max_length=100)
   language = models.CharField(max_length=100)


class Flower(models.Model):
   name = models.CharField(max_length=100)
   lifetime = models.CharField(max_length=10)
   color = models.CharField(max_length=10)
   species = models.ForeignKey(Species, on_delete=models.DO_NOTHING)