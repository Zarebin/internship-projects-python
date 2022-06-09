from django.db import models
from django.contrib.auth import get_user_model





User = get_user_model()



class FoodQuestion (models.Model):
    '''The values we send from the user'''

    question = models.TextField()
    image_url = models.ImageField( height_field=None, width_field=None)
    language = models.CharField(max_length=2)
    response_count = models.PositiveIntegerField(default=0)   #Indicates how many we have requested


class FoodResponse (models.Model):
    '''The values get to the user'''

    USER_CHOISE = (                     
          
            ('0','Top'), ('1', 'Bottom'),
            ('2', 'Similar'),('3', 'Skip')
        )
        
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    qustion = models.ForeignKey( on_delete=models.CASCADE,)
    response = models.CharField(max_length=2,choices = USER_CHOISE)

