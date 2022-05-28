from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth import get_user_model

# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import QuestionSerializer
from .serializers import AnswerSerializer

from .models import Question
from .models import Answer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
