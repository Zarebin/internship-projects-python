from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated


from .models import FoodLabel, Food
from .serializer import FoodLabelSerializer, FoodSerializer

def test(request):
    return JsonResponse({'message': 'food label'})



class FoodLabelAPI(GenericViewSet):

    permission_classes = [IsAuthenticated]   

    def get_queryset(self): 
        if self.action == "create":
            return FoodLabel.objects.all()
        elif self.action == "list":
            return Food.objects.filter(answer_count__lte = 3)
        elif self.action == "retrieve":
            return Food.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return FoodLabelSerializer
        elif self.action == "list":
            return FoodSerializer
        elif self.action == "retrieve":
            return FoodSerializer

    def create(self, request, *args, **kwargs):
        serializer =  self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        query_set = self.get_queryset()
        serializer = self.get_serializer(query_set,many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        query_set = self.get_queryset()
        instance = get_object_or_404(query_set,pk=pk)
        serializer = self.get_serializer(instance)
        return Response(serializer.data) 


