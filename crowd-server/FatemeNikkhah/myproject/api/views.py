from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from food.models import Question
from .serializers import QuestionSerializer,ResponseSerializer


@api_view(['GET'])
def get_food_fact(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions,many = True)
    return Response(serializer.data)

@api_view(['POST'])
def send_response(request):
    serializer = ResponseSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)