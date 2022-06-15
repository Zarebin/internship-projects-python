from django.apps import AppConfig


class CustomUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crowd_server.apps.custom_user'
