from rest_framework import serializers
from .models import Question,Answer


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
    
        model = Question
        fields = ['language','img_url' ,'question','response_count']       

class AnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Answer
        fields = '__all__'         

    def create(self, validated_data):

        question = validated_data['question']
        question.response_count += 1                       
        question.save()
        return  Answer.objects.create(**validated_data)        
