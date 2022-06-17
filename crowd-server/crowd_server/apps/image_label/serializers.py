from rest_framework import serializers
from .models import Category, ImageLabel, Image


class ImageCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name', 'question', 'image_path']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id','category', 'path', 'answer_count']


class ImageLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageLabel
        fields = ['user', 'image', 'answer']

    def create(self, validated_data):
        image = validated_data['image']
        image.answer_count += 1
        image.save()
        return ImageLabel.objects.create(**validated_data)    
