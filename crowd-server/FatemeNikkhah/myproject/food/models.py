from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Question(models.Model):
    question = models.TextField()
    image_url =models.TextField()
    language = models.CharField(max_length=15)
    question_id = models.PositiveIntegerField(primary_key=True)


class Response(models.Model):

    id = models.AutoField(primary_key=True)
    fact = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(3)])
    user_id = models.PositiveIntegerField(default = 0
    )
    # user_id =models.ForeignKey(User)