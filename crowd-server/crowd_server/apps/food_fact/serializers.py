from rest_framework import serializers


class FoodQuestionSerialiser(serializers.Serializer):
    
    question = serializers.CharField ()
    image_url = serializers.ImageField ()
    language = serializers.CharField ()
    response_count = serializers.IntegerField ()         #if write_only = True : Never show in response 

    


class FoodResponseSerialiser(serializers.Serializer):

    user = serializers.CharField(required=True,)
    response = serializers.CharField(required=True)
    qustion = serializers.CharField(required=True)
    

