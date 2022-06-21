from rest_framework import serializers
from .models import FoodLabel, Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['image_path', 'answer_count', 'language']


class FoodLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodLabel
        fields = ['user', 'image', 'answer']

    def create(self, validated_data):
        image = validated_data['image']
        image.answer_count += 1
        image.save()
        return FoodLabel.objects.create(**validated_data)