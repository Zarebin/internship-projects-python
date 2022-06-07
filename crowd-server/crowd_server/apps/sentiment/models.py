from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
PREVIOUS = "previous"
NEGATIVE = "negative"
NEUTRAL = "neutral"
POSITIVE = "positive"
SKIP = "skip"

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
    number_of_answers = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.text


class EvaluatedSentiment(models.Model):
    question = models.ForeignKey(Question, related_name='evaluated_sentiments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='evaluated_sentiments', on_delete=models.CASCADE)
    value = models.CharField(max_length=10 , choices=ANSWER_CHOICES)
