from django.urls import path
from .views import ImageViewAPI, ImageCategoryView

urlpatterns = [
    path('categories/', ImageCategoryView.as_view()),
    path('image/', ImageViewAPI.as_view())
]