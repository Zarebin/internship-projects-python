from rest_framework import serializers
from .models import Answer, Question


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('question', 'user', 'fact')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('image_url', 'text', 'language')
