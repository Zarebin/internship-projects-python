from rest_framework import serializers

from crowd_api.models import Flower, Species

class FlowerSerializer(serializers.ModelSerializer):
   class Meta:
       model = Flower
       fields = ('name', 'lifetime', 'color', 'species')


class SpeciesSerializer(serializers.ModelSerializer):
   class Meta:
       model = Species
       fields = ('name', 'classification', 'language')