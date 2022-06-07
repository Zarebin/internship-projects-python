from django.urls import path, include
from .views import SentimentAPI
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api', SentimentAPI, basename="api")

urlpatterns = router.urls
