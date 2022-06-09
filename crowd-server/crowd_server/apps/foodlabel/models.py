
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class FoodCategory(models.Model):
    name = models.CharField(max_length=255)
    question = models.TextField()
    food_path = models.FoodField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.question}"


class Food(models.Model):
    food_category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name='foods')
    path = models.FoodField()
    answer_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.path}"


class FoodLabel(models.Model):
    class Answer(models.IntegerChoices):
        YES = 0
        NO = 1
        NOT_SURE = 2
        SKIPPED = 3

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='food_labels')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='food_labels')
    answer = models.IntegerField(choices=Answer.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.answer}"
