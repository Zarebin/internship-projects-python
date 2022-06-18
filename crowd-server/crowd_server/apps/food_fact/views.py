from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question
from .serializers import QuestionSerializer,ResponseSerializer
from rest_framework import status



class QuestionView(APIView):
    

    def get(self,request):

        '''The values we send from the user'''
        question = Question.objects.all()
        srz_data = QuestionSerializer(instance=question,many =True)       

        return Response({'data':srz_data.data},status.HTTP_202_ACCEPTED )   

      
    def post (self,request):

        '''The values get to the user'''
        srz_data= ResponseSerializer(data=request.data)

        '''If the user's answer is correct and without any problems, it will be saved'''
        if srz_data.is_valid():
            srz_data.save()

            return Response({'data':srz_data.data},status=status.HTTP_201_CREATED)  
               
        return Response(srz_data.errors,status=status.HTTP_400_BAD_REQUEST)  
  

  






