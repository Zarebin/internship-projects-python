from django.urls import include, path

from rest_framework import routers

from crowd_api.views import FlowerViewSet, SpeciesViewSet

router = routers.DefaultRouter()
router.register(r'flower', FlowerViewSet)
router.register(r'species', SpeciesViewSet)

urlpatterns = [
   path('', include(router.urls)),
