from django.urls import path
from .views import Food

urlpatterns = [
    path('food_fact/',Food.as_view())
]

