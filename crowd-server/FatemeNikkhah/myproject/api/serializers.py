from django.db.models import fields
from rest_framework import serializers
from food.models import Question,Response

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields ='__all__'