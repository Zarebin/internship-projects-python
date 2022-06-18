from .base import *
from celery.schedules import crontab
import crowd_server.tasks

INSTALLED_APPS += ["django_celery_beat"]
CELERY_BROKER_URL = "redis://redis:6379"
CELERY_RESULT_BACKEND = "redis://redis:6379"