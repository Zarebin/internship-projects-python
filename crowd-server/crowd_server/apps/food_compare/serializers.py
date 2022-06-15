from rest_framework import serializers
from .models import CompareQuestion,Comparison,Profile


class ProfileSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(source = "user.first_name")
    last_name = serializers.CharField(source = "user.last_name")
    bio = serializers.CharField(source = "user.bio")
    birthday = serializers.DateField(source = "user.birthday")
    profile_pic = serializers.ImageField(source = "user.profile_pic")
    gender = serializers.CharField(source = "user.gender")
    class Meta:
        model = Profile
        fields = ("user","first_name","last_name","bio","birthday","profile_pic","gender")

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
