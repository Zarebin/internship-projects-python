from django.urls import path

from crowd_app.views import FoodFactAPIView

urlpatterns = [
    path('foodfact/', FoodFactAPIView.as_view()),
]