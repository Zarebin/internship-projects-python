from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class ImageCategory(models.Model):
    name = models.CharField(max_length=255)
    question = models.TextField()
    image_path = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.question}"


class Image(models.Model):
    image_category = models.ForeignKey(ImageCategory, on_delete=models.CASCADE, related_name='images')
    path = models.ImageField()
    answer_count = models.PositiveIntegerField(default=0)
    verified = models.BooleanField(null=True,default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.path}"


class ImageLabel(models.Model):
    class Answer(models.IntegerChoices):
        YES = 0
        NO = 1
        NOT_SURE = 2
        SKIPPED = 3

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='image_labels')
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='image_labels')
    answer = models.IntegerField(choices=Answer.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.answer}"


class UserScore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    value = models.SmallIntegerField(null=False,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"score = {self.value}"