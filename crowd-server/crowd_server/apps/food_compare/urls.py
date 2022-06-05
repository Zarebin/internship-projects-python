from django.urls import path
from .views import test,CompareFoodAPI,CompareFoodAPI2
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("comparefood",CompareFoodAPI,basename="comparefood")

urlpatterns = [
    path('test/', test, name="test"),
    path('',CompareFoodAPI2.as_view()),
]+router.urls