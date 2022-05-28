from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .serializers import AnswerSerializer,QuestionSerializer
from .models import Question


class FoodFactAPIView(APIView):

    def get(self, request):
        question_id = request.data['question_id']
        question = get_object_or_404(Question, id=question_id)
        question_serializer = QuestionSerializer(instance=question)
        data = question_serializer.data
        return Response({'question': data}, status=status.HTTP_200_OK)

    def post(self, request):
        answer_serializer = AnswerSerializer(data=request.data)
        if answer_serializer.is_valid():
            answer_serializer.save()
            return Response({'message': 'Answer added successfully!'}, status=status.HTTP_201_CREATED)

        return Response({'message': answer_serializer.errors}, status=400)


