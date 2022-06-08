from django.urls import path
from .views import food_fact

urlpatterns = [
    path('food_fact/',food_fact)
]

