from django.urls import path, include
from .views import SentimentAPI
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', SentimentAPI, basename="sentiment")

urlpatterns = router.urls
