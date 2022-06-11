from rest_framework import serializers
from .models import Question, Evaluatedtranslation


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['text','text', 'language', 'answers']


class EvaluatedTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluatedtranslation
        fields = ['question', 'user', 'value']

    def create(self, validated_data):
        question = validated_data['question']
        question.answers += 1
        question.save()
        return Evaluatedtranslation.objects.create(**validated_data)
