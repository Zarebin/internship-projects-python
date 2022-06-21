from django.urls import path
from views import goodbye_view, hello_view

urlpatterns = [
    path("good-bye/", goodbye_view, name="goodbye"),
    path("", hello_view, name="hello"),
]