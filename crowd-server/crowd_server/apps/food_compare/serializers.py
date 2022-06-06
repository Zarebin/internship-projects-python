from rest_framework import serializers
from .models import CompareQuestion,Comparison
from django.db.models import F

class CompareQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompareQuestion
        fields = ("language","question","response_count")

    def create(self, validated_data):
        return CompareQuestion(**validated_data)


class ComparisonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comparison
        fields = ("user","question","response")

    def create(self, validated_data):
        question_content = validated_data['question']
        print(question_content)
        question = CompareQuestion.objects.get(question = question_content)
        question.response_count = F('response_count') + 1
        question.save()
        return Comparison(**validated_data)
