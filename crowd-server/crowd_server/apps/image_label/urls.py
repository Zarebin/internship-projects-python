from django.urls import path
from .views import ImageLabelView, ImageCategoryView, ImageView

urlpatterns = [
    path('categories/', ImageCategoryView.as_view()),
    path('image/', ImageView.as_view()),
    path('label/', ImageLabelView.as_view())
]