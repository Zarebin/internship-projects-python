from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    LANGUAGES = [
        ('en', 'English'),
        ('fa', 'Farsi'),
    ]
    question = models.CharField(max_length=300)
    image_url = models.CharField(max_length=300)
    language = models.CharField(choices=LANGUAGES, max_length=2)

    def __str__(self):
        return f"{self.question}"


class Answer(models.Model):
    class Fact(models.IntegerChoices):
        YES = 0
        NO = 1
        NOT_SURE = 2
        SKIPPED = 3

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    fact = models.IntegerField(choices=Fact.choices)

    def __str__(self):
        return f"{self.question.question} , fact:{self.fact}"
