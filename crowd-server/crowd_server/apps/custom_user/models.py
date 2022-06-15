from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from datetime import datetime

class UserManager(BaseUserManager):
    use_in_migrations = True

    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})
        
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('email field is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
     
    username = None
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

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


