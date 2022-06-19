from django.urls import path, include
from .views import test, FoodLabelAPI
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'api', FoodLabelAPI, basename="api")

urlpatterns = router.urls

urlpatterns = [
    path ('test/', test, name = "test")
] +router.urls    
