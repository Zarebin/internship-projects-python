from rest_framework import serializers
from .models import *


class QuestionSerialiser(serializers.ModelSerializer):


    class Meta:
        
        model = Question
        fields = ['id','language','img_url' ,'question','response_count']        # ->['language','img_url' ,'question','response_count']

   


class ResponseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Response
        fields = '__all__'          # ->[ user, response, question ]

        # extra_kwargs={
        # 'user' : {'require':True},
        # 'response' : {'require':True},
        # 'question' : {'require':True},
        # }
        
        
    def create(self, validated_data):

        question_content = validated_data['question']
        question = Question.objects.get(id = question_content.id)
        question.response_count += 1                        #One is added with each answer
        question.save()

        return Question(**validated_data)        

