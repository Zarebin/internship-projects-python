from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from .models import Question, EvaluatedSentiment
from .serializers import QuestionSerializer, EvaluatedSentimentSerializer


# Create your views here.
class SentimentAPI(GenericViewSet):

    def get_queryset(self):
        if self.action == "create":
            return EvaluatedSentiment.objects.all()
        elif self.action == "retrieve":
            return Question.objects.filter(number_of_answers__lt=3)
        elif self.action == "list":
            return Question.objects.filter(number_of_answers__lt=3)

    def get_serializer_class(self):
        if self.action == "create":
            return EvaluatedSentimentSerializer
        elif self.action == "retrieve":
            return QuestionSerializer
        elif self.action == "list":
            return QuestionSerializer

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        question = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(question)
        response = Response(serializer.data, status=status.HTTP_200_OK)

        return response

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class SentimentAPI2(APIView):

    def get(self, request):
        queryset = Question.objects.filter(number_of_answers__lt=3)
        question = get_object_or_404(queryset, pk=request.data['id'])
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def post(self, request):
        serializer = EvaluatedSentimentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        question = Question.objects.get(id=request.data['question'])
        question.number_of_answers += 1
        question.save()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


