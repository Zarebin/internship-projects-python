from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    '''The values we send from the user'''

    language = models.CharField(max_length=10)
    img_url = models.ImageField()
    question = models.TextField()
    response_count = models.PositiveIntegerField(default=0)

    def __str__(self) :
        return f'{self.language} - {self.question}'


class Response (models.Model):
    '''The values get to the user'''

    USER_CHOISE = (                     
           
            ('0','Top'), ('1', 'Bottom'),
            ('2', 'Similar'),('3', 'Skip')
        )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Response')
    response = models.CharField(max_length=2,choices = USER_CHOISE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='Response')


    