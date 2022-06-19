from celery import shared_task
from celery.utils.log import get_task_logger
from celery.schedules import crontab
from django.core.management import call_command 
from .models import UserScore, Image, ImageLabel

import crowd_server.apps.image_label.tasks

logger = get_task_logger(__name__)

@shared_task
def sample_task():                    
    logger.info("The sample task just ran.")

@shared_task
def send_email_report():
    call_command("email_report", )    