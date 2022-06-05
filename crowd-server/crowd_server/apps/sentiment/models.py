from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
PREVIOUS = "0"
NEGATIVE = "1"
NEUTRAL = "2"
POSITIVE = "3"
SKIP = "4"

ANSWER_CHOICES = (
    (PREVIOUS, "Previous"),
    (NEGATIVE, "Negative"),
    (NEUTRAL, "Neutral"),
    (POSITIVE, "Positive"),
    (SKIP, "Skip")
)


class Question(models.Model):
    text = models.TextField()
    language = models.CharField(max_length=20)
    number_of_answers = models.IntegerField(default=0)

    def __str__(self):
        return self.text


class EvaluatedSentiment(models.Model):
    question = models.ForeignKey(Question, related_name='evaluatedSentiments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='evaluatedSentiments', on_delete=models.CASCADE)
    value = models.CharField(max_length=2, choices=ANSWER_CHOICES)
