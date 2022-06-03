from django.urls import path, include
from .views import SentimentAPI, SentimentAPI2
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api', SentimentAPI, basename="api")

urlpatterns = router.urls

""""
urlpatterns = [
   path('', SentimentAPI2.as_view())
]
"""