from rest_framework import status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Question, EvaluatedSentiment
from .serializers import QuestionSerializer, EvaluatedSentimentSerializer
from rest_framework.permissions import IsAuthenticated


class SentimentAPI(GenericViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.action == "create":
            return EvaluatedSentiment.objects.all()
        elif self.action == "list":
            return Question.objects.filter(number_of_answers__lt=3)

    def get_serializer_class(self):
        if self.action == "create":
            return EvaluatedSentimentSerializer
        elif self.action == "list":
            return QuestionSerializer

    def create(self, request, *args, **kwargs):
        data = {
            'question': self.request.data['question'],
            'value': self.request.data['value'],
            'user': self.request.user.id
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(language=request.data['language'])
        user_answers = EvaluatedSentiment.objects.filter(user_id=self.request.user.id).values_list('question',
                                                                                                   flat=True)

        try:
            question = queryset.exclude(id__in=user_answers).order_by('-number_of_answers').first()
            serializer = self.get_serializer(question)
            response = Response(serializer.data, status=status.HTTP_200_OK)
            return response
        except question.DoesNotExist:
            response = Response(status=status.HTTP_404_NOT_FOUND)
            return response
