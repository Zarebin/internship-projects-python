from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator

# Create your models here.

User = get_user_model()

class CompareQuestion(models.Model):

    language = models.CharField(max_length=10)
    top_img_url = models.ImageField()
    bottom_img_url = models.ImageField()
    question = models.TextField()
    response_count = models.IntegerField(default=0,validators=[MaxValueValidator(3)])
    

    def __str__(self):
        return self.question

class Comparison(models.Model):

    RESPONSE_CHOICE = (
            ('0','Top'),
            ('1', 'Bottom'),
            ('2', 'Similar'),
            ('3', 'Skip'),
        )
    response = models.CharField(max_length=2,choices=RESPONSE_CHOICE)
    question = models.ForeignKey(CompareQuestion, on_delete=models.CASCADE, related_name='Comparison')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='Comparison')
    

