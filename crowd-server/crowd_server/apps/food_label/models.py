from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()


class Food(models.Model):
    language = models.CharField(max_length=10)
    question = models.TextField()
    image_path = models.ImageField()
    answer_count = models.PositiveIntegerField(default=0)
    

    def __str__(self):
        return f"{self.image_path}"


class FoodLabel(models.Model):
    class Answer(models.Choices):
        YES = "yes"
        NO = "no"
        NOT_SURE = "Not sure"
        SKIPPED = "Skip"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='food_labels')
    image = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='food_labels')
    answer = models.CharField(choices=Answer.choices, max_length=10)
   

    def __str__(self):
        return f"{self.user.username} - {self.answer}"
