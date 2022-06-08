from rest_framework import serializers


class UserInSerialiser(serializers.Serializer):
    
    question_id = serializers.CharField (required=True,write_only=True)         #if write_only = True : Never show in response 
    question = serializers.CharField (required=True,)
    image_url = serializers.ImageField (required=True,)
    language = serializers.CharField (required=True,)

    def validate(self,data):

        value = data['language']
        if value != 'fa' or value != 'en' :

            raise serializers.ValidationError ('your language must be fa(Persian) or en(English)')

        return data


class UserOutSerialiser(serializers.Serializer):

    user_id = serializers.CharField(required=True,read_only=True)
    response = serializers.CharField(required=True)

