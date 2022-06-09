from django.urls import path
from .views import test,FoodLabelAPI
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('',FoodLabelAPI,basename="foodlabel")

urlpatterns = [
    path('test/', test, name="test"),
]+router.urls