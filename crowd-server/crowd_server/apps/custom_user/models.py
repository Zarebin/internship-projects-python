from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class User(AbstractUser):  

    username = models.CharField(max_length=20,unique=True)
    email = models.EmailField(unique=True)

    GENDER_CHOICE = (
            ('f','Female'),
            ('m', 'Male'),
            ('p', 'Prefer not to say'),
        )

    bio = models.TextField(default="Bio")
    profile_pic = models.ImageField(default='default.jpg',upload_to='profile_images')
    birthday = models.DateField(default=datetime.now)
    gender = models.CharField(max_length=20,choices=GENDER_CHOICE,default = "p")

