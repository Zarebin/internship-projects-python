from rest_framework import serializers
from . models import Question,EvaluatedTranslation

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields='__all__'

class EvaluatedTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model=EvaluatedTranslation
        fields='__all__'
    def create(self, validated_data):
        question = validated_data['question']
        question.number_of_sent_answers += 1
        question.save()
        return EvaluatedTranslation.objects.create(**validated_data)