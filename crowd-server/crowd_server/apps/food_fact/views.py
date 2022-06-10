from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status


class QuestionView(APIView):

    def get(self,request):

        question = Question.objects.all()
        srz_data = QuestionSerialiser(instance=question,many=True)


        return Response (srz_data.data,status=status.HTTP_202_ACCEPTED)


       

    def post (self,request):
        
        
        srz_data= ResponseSerializer(data= request.POST)
        if srz_data.is_valid():

            srz_data.save()
            return Response(srz_data.data,status=status.HTTP_201_CREATED)

        return Response (srz_data.error,status=status.HTTP_400_BAD_REQUEST)










