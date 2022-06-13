from rest_framework import serializers
from .models import QuestionModel,ResponseModel


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
    
        model = QuestionModel
        fields = ['language','img_url' ,'question','response_count']       

class ResponseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ResponseModel
        fields = '__all__'         

    def create(self, validated_data):

        question = validated_data['question']
        question.response_count += 1                       
        question.save()
        return  ResponseModel.objects.create(**validated_data)        
