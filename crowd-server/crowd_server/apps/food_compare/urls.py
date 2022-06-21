from django.urls import path
from .views import test,CompareFoodAPI
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('',CompareFoodAPI,basename="comparefood")

urlpatterns = [
    path('test/', test, name="test"),
]+router.urls