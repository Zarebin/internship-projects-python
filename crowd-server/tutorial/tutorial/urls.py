from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('tutorial.quickstart.urls')),
    path('blog/', include('tutorial.blog.urls')),
    path('admin/', admin.site.urls),
]