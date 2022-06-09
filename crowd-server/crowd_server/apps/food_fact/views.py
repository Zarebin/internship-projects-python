
from django.urls import is_valid_path
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FoodQuestion,FoodResponse
from .serializers import FoodQuestionSerialiser,FoodResponseSerialiser




class Food (APIView):


    def get (self,request) :

        food_question = FoodQuestion.objects.all()
        ser_data = FoodQuestionSerialiser(instance=food_question)

        return Response (data=ser_data.data)



    def post (self,request):
        
        food_response = FoodResponseSerialiser(data=request.POST)

        if FoodResponseSerialiser.is_valid():
            
            FoodResponseSerialiser.save()


            return Response (FoodResponseSerialiser.data,status=status.HTTP_201_CREATED)

     


        








# @api_view(['POST','GET'])
# def food_fact(resuest):

#     if resuest.method == 'GET':
#         '''If the request items are of type (GET), our question will be sent to the user'''

#         result = UserIn.objects.all()
#         serializer_get = UserInSerialiser(instance=result)

#         return Response({'message':'sent'})

#     else:

#         '''If the request is of type (POST), the answer will be sent to the user'''
#         serializer_post_data = UserOutSerialiser(data=resuest.POST)

#         if serializer_get.is_valid():

#             serializer_get.save()

#             return Response(status=status.HTTP_200_OK)



