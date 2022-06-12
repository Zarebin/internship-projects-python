from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question,Response
from .serializers import QuestionSerialiser,ResponseSerializer
from rest_framework import status
from django.http import JsonResponse


class QuestionView(APIView):

    def get(self,request):

        '''The values we send from the user'''
        question = Question.objects.all()
        srz_data = QuestionSerialiser(instance=question,many =True)       

        return JsonResponse({'data':srz_data.data},status=status.HTTP_202_ACCEPTED )   #,status.HTTP_202_ACCEPTED   

      
    def post (self,request):
        '''The values get to the user'''
        srz_data= ResponseSerializer(data = request.POST)

        '''If the user's answer is correct and without any problems, it will be saved'''
        if srz_data.is_valid():

            srz_data.save()
            return JsonResponse({'data':srz_data.data},status=status.HTTP_201_CREATED)  
        
        else:
            return JsonResponse({'message':'Bad request'},status=status.HTTP_400_BAD_REQUEST)  
  

  






