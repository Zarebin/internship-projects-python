from celery import shared_task
from celery.utils.log import get_task_logger
from celery.schedules import crontab
from django.core.management import call_command


import crowd_server.apps.image_label.tasks

logger = get_task_logger(__name__)


@shared_task
def calculate_image_label_scores_task():
    from .models import UserScore, Image, UserAnswer

    images = Image.objects.filter(answer_count__gte=3, verified=None).all()

    for image in images:
        user_answers = UserAnswer.objects.filter(image_id=image.id,
                                                 answer__in=[
                                                     UserAnswer.Answer.YES,
                                                     UserAnswer.Answer.NO
                                                 ]).all()
        answers = [i['answer'] for i in list(user_answers.values('answer'))]
        vote_result = max(answers, key=answers.count)
        image.verified = vote_result == UserAnswer.Answer.YES or False
        image.save()
        for user_answer in user_answers:
            uscore, _ = UserScore.objects.get_or_create(
                user_id=user_answer.user.id)
            if user_answer.answer == vote_result:
                uscore.value += 10
            else:
                uscore.value -= 10
            uscore.save()

    logger.info("Scores Calculated Successfully")
    return True
