"""crowd_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('image-label/', include('crowd_server.apps.image_label.urls')),
    path('sentiment/', include('crowd_server.apps.sentiment.urls')),
    path('food_label/', include('crowd_server.apps.food_label.urls')),
    path('food_compare/', include('crowd_server.apps.food_compare.urls')),
    path('translation_evaluator/', include('crowd_server.apps.translation_evaluator.urls')),
    path('food_fact/', include('crowd_server.apps.food_fact.urls')),
]

