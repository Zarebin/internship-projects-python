from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import ImageSerializer, ImageLabelSerializer, ImageCategorySerializer
from .models import Category, Image, ImageLabel


class ImageCategoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        categories = Category.objects.all()
        serializer = ImageCategorySerializer(categories, many=True)

        return Response(serializer.data)


class ImageViewAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        image_labels = ImageLabel.objects.filter(user_id = self.request.user.id).values('image_id')
        image = Image.objects.filter(answer_count__lt=3).exclude(id__in=image_labels).order_by('-answer_count').first()
        serializer = ImageSerializer(image)
        return Response(serializer.data)

    def post(self, request):
        serializer = ImageLabelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)  
