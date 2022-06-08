from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import UserIn
from .serializers import UserInSerialiser,UserOutSerialiser




@api_view(['POST','GET'])
def food_fact(resuest):

    if resuest.method == 'GET':
        '''If the request items are of type (GET), our question will be sent to the user'''

        result = UserIn.objects.all()
        serializer_get_data = UserInSerialiser(instance=result)

        return Response({'message':'sent'})

    else:
        '''If the request is of type (POST), the answer will be sent to the user'''
        serializer_post_data = UserOutSerialiser(data=resuest.POST)

        if serializer_get_data.is_valid:

            serializer_get_data.save()

            return Response(status=status.HTTP_202_ACCEPTED)



