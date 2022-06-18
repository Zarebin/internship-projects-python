import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crowd_server.settings.production")
app = Celery("crowd_server")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
