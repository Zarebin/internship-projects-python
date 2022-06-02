from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import ImageSerializer, ImageLabelSerializer, ImageCategorySerializer
from .models import ImageCategory, Image


class ImageCategoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        categories = ImageCategory.objects.all()
        serializer = ImageCategorySerializer(categories, many=True)
        return Response(serializer.data)


class ImageView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        image = Image.objects.filter(answer_count__lt=3).last()
        serializer = ImageSerializer(image)
        return Response(serializer.data)


class ImageLabelView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ImageLabelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
