from django.db import models



class UserIn(models.Model):
    '''The values we get from the user'''

    question_id = models.CharField(max_length=100)
    question = models.TextField()
    image_url = models.ImageField( height_field=None, width_field=None)
    language = models.CharField(max_length=20)



class UserOut (models.Model):
    '''The values ​​we send to the user'''

    USER_CHOISE = (                     
            '''Items in which the user has the right to choose'''
            ('0','Top'), ('1', 'Bottom'),
            ('2', 'Similar'),('3', 'Skip')
        )
    
    user_id = models.CharField(100)
    response = models.CharField(max_length=2,choices = USER_CHOISE)


    
