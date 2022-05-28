from django.db import models
from django.contrib.auth.models import AbstractUser

ANSWER_CHOICES = (
    ("0", "yes"),
    ("1", "no"),
    ("2", "notSure"),
    ("3", "skip")
)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)


class Question(models.Model):
    image_url = models.CharField(max_length=60)
    text = models.TextField()
    language = models.CharField(max_length=20)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name='answers', on_delete=models.CASCADE)
    fact = models.CharField(max_length=2, choices=ANSWER_CHOICES)
