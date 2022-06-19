from rest_framework import serializers
from .models import Question,answer


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
    
        model = Question
        fields = ['language','img_url' ,'question','response_count']       

class ResponseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = answer
        fields = '__all__'         

    def create(self, validated_data):

        question = validated_data['question']
        question.response_count += 1                       
        question.save()
        return  answer.objects.create(**validated_data)        
