from django.apps import AppConfig


class FoodCompareConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crowd_server.apps.food_compare'

    def ready(self):
        import crowd_server.apps.food_compare.signals