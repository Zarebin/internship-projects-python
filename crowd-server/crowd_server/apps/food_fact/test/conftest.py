import pytest


@pytest.fixture(scope='session')
def django_db_setup():
        from django.conf import settings
        settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'db.example.com',
        'NAME': 'external_db',
    }


@pytest.fixture
def api_client():
   from rest_framework.test import APIClient
   return APIClient()

@pytest.fixture
def user_data():
   return { "user" : "1","response" : "1","question" : "1"}