from rest_framework import serializers
from .models import Question, EvaluatedSentiment


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['text', 'language', 'number_of_answers']


class EvaluatedSentimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluatedSentiment
        fields = ['question', 'user', 'value']

    def create(self, validated_data):
        question = validated_data['question']
        question.number_of_answers += 1
        question.save()
        return EvaluatedSentiment.objects.create(**validated_data)

