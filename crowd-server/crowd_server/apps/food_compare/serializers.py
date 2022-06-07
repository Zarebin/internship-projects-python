from rest_framework import serializers
from .models import CompareQuestion,Comparison


class CompareQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompareQuestion
        fields = ("language","question","response_count")


class ComparisonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comparison
        fields = ("user","question","response")

    def create(self, validated_data):
        question_content = validated_data['question']
        question = CompareQuestion.objects.get(id = question_content.id)
        question.response_count += 1
        question.save()
        return Comparison(**validated_data)
