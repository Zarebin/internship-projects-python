from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class QuestionModel(models.Model):

    '''The values we send from the user'''
    id = models.AutoField(blank=False, primary_key=True)
    language = models.CharField(max_length=2,)
    img_url = models.ImageField()
    question = models.TextField()
    response_count = models.PositiveIntegerField(default=0)  

    def __str__(self) :
        return f' {self.id}'


class ResponseModel(models.Model):
    '''The values get to the user'''

    USER_CHOISE = (                                         
            ('0','Yes'),
            ('1', 'No'),
            ('2', 'Not Sure'),
            ('3', 'Skip') )

    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='Response',blank=True)
    response = models.CharField(max_length=2,choices = USER_CHOISE)
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE, related_name='Response',default=1)

    
    
