from rest_framework import serializers
from .models import ImageCategory, ImageLabel, Image


class ImageCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageCategory
        fields = ['name', 'question', 'image_path']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image_category', 'path', 'answer_count']


class ImageLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageLabel
        fields = ['user', 'image', 'answer']

    def create(self, validated_data):
        image = validated_data['image']
        #FIXME : counter add if imagelabel answer is yes or no
        image.answer_count += 1
        image.save()
        return ImageLabel.objects.create(**validated_data)    
