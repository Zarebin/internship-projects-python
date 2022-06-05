from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Comparison,CompareQuestion

from .serializers import ComparisonSerializer,CompareQuestionSerializer

def test(request):
    return JsonResponse({'message': 'food compare'})


class CompareFoodAPI2(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):  
        question = CompareQuestion.objects.all()
        serializer = CompareQuestionSerializer(question,many=True)
        return Response(serializer.data)
        
    def post(self,request):   
        serializer = ComparisonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


class CompareFoodAPI(ModelViewSet):

    def get_queryset(self): 
        if self.action == "create":
            return Comparison.objects.all()
        elif self.action == "list":
            return CompareQuestion.objects.all()
        elif self.action == "retrieve":
            return CompareQuestion.objects.filter(id = 5)

    def get_serializer(self):  
        if self.action == "create":
            return ComparisonSerializer
        elif self.action == "list":
            return CompareQuestionSerializer
        elif self.action == "retrieve":
            return CompareQuestionSerializer

    def create(self, request, *args, **kwargs):
        serializer =  self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        query_set = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(query_set,many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        query_set = self.filter_queryset(self.get_queryset())
        question = get_object_or_404(query_set, pk=pk)
        serializer = self.get_serializer(question)
        return Response(serializer.data)
