from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

User = get_user_model()

class CompareQuestion(models.Model):

    language = models.CharField(max_length=10)
    top_img_url = models.ImageField()
    bottom_img_url = models.ImageField()
    question = models.TextField()
    response_count = models.PositiveIntegerField(default=0)
    

    def __str__(self):
        return self.question

class Comparison(models.Model):

    RESPONSE_CHOICE = (
            ('top','Top'),
            ('bottom', 'Bottom'),
            ('similar', 'Similar'),
            ('skip', 'Skip'),
        )
    response = models.CharField(max_length=7,choices=RESPONSE_CHOICE)
    question = models.ForeignKey(CompareQuestion, on_delete=models.CASCADE, related_name='comparison')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comparison')
    

