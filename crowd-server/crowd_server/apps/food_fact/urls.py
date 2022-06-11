from django.urls import path
from .views import QuestionView

urlpatterns = [
    path('food/',QuestionView.as_view())
]


