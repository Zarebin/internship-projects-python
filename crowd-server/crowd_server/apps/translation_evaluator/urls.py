from django.urls import path, include
from .views import translateAPI
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api', translateAPI, basename="api")

urlpatterns = router.urls