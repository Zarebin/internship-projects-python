from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Question(models.Model):
    question_text = models.TextField()
    answer_text = models.TextField()
    language = models.CharField(max_length=20)
    number_of_sent_answers = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Question:{self.question_text},Answer:{self.answer_text}"


class EvaluatedTranslation(models.Model):
    class Answer(models.IntegerChoices):
        YES = 0
        NO = 1
        SKIPPED = 3

    question = models.ForeignKey(Question, related_name='evaluated_translation', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='evaluated_translation', on_delete=models.CASCADE)
    value = models.IntegerField(choices=Answer.choices)



