from django.urls import path
from .views import test,CompareFoodAPI,ProfileAPI
from rest_framework.routers import DefaultRouter




router = DefaultRouter()
router.register(r'food_compare',CompareFoodAPI,basename="comparefood")
router.register(r'profile',ProfileAPI,basename="profile")

urlpatterns = [
    path('test/', test, name="test"),
]+router.urls
