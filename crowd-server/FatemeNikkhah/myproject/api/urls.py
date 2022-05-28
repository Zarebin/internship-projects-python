from django.urls import path
from . import views

urlpatterns =[
    path('',views.get_food_fact),
    path('post/',views.send_response)
]