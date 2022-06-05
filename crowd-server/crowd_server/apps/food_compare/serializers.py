from rest_framework import serializers
from .models import CompareQuestion,Comparison


class CompareQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompareQuestion
        fields = ("id","question")


class ComparisonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comparison
        fields = ("user","question","response")

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def save(self, **kwargs):
        return super().save(**kwargs)