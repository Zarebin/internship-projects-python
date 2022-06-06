from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Comparison,CompareQuestion
from .serializers import ComparisonSerializer,CompareQuestionSerializer

def test(request):
    return JsonResponse({'message': 'food compare'})



class CompareFoodAPI(ModelViewSet):

    permission_classes = [IsAuthenticated]   

    def get_queryset(self): 
        if self.action == "create":
            return Comparison.objects.all()
        elif self.action == "list":
            return CompareQuestion.objects.filter(response_count__lte = 3)
           

    def get_serializer_class(self):
        if self.action == "create":
            return ComparisonSerializer
        elif self.action == "list":
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

