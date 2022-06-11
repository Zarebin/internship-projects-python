from django.urls import path
from .views import QuestionView





urlpatterns = [
    path('food_fact/',QuestionView.as_view())
]


