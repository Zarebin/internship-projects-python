from rest_framework import serializers
from .models import Question,Response


class QuestionSerialiser(serializers.ModelSerializer):

    class Meta:
    
        model = Question
        fields = ['language','img_url' ,'question','response_count']       

class ResponseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Response
        fields = '__all__'         

        extra_kwargs={
        'user' : {'require':True},
        'response' : {'require':True},
        'question' : {'require':True}, }
        
    def create(self, validated_data):

        question = validated_data['question']
        question.response_count += 1                       
        question.save()
        return Response.objects.create(**validated_data)        

