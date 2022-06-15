from django.db import models
from django.contrib.auth import get_user_model
from django.utils.html import format_html


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
    

class Profile(models.Model):
    
    GENDER_CHOICE = (
            ('f','Female'),
            ('m', 'Male'),
            ('p', 'Prefer not to say'),
        )
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    
    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def bio(self):
        return self.user.bio
    
    def profile_pic(self):
        return self.user.profile_pic
    
    def birthday(self):
        return self.user.birthday
    
    def gender(self):
        return self.user.gender

    def profile_img_preview(self):
            return format_html('<img src="{}" height="60" width ="60" />'.format(self.user.profile_pic.url))

