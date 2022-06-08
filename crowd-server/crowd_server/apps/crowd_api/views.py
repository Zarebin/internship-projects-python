from django.shortcuts import render

from rest_framework import viewsets

from crowd_api.serializers import FlowerSerializer, SpeciesSerializer
from crowd_api.models import Flower, Species


class PersonViewSet(viewsets.ModelViewSet):
   queryset = Flower.objects.all()
   serializer_class = FlowerSerializer


class SpeciesViewSet(viewsets.ModelViewSet):
   queryset = Species.objects.all()
   serializer_class = SpeciesSerializer
