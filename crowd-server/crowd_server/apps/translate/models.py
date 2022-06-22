from unittest import skip
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
previous = "previous"
next="next"
Skip ="skip"
true="true"
false="false"
ANSWER_CHOICES = (
    (previous, "previous"),
    (next, "next"),
    (Skip, "skip"),
    (true, "true"),
    (false, "false")
)


class Question(models.Model):
    text = models.TextField()
    text = models.TextField()
    language = models.CharField(max_length=20)
    answers = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.text


class Evaluatedtranslation(models.Model):
    question = models.ForeignKey(Question, related_name='evaluated_translation', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='evaluated_translation', on_delete=models.CASCADE)
    value = models.CharField(max_length=10 , choices=ANSWER_CHOICES)