from djoser.serializers import UserCreateSerializer,UserSerializer


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['username','password','email','first_name','last_name','bio', 'profile_pic', 'birthday','gender']

class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ['email','first_name','last_name']