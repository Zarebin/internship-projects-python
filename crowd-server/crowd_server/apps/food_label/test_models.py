
import pytest
from django.contrib.auth.models import User
from .models import Food, FoodLabel

@pytest.mark.rest_framework_db

def test_food_create():
    food = Food.objects.create(
    language = "en",
    question = "Is Alo Signature Corn Flake Crusted French Toast the dish shown in the image?", 
    image_path = "Toast"

    )
    assert food.language == "en"
    assert food.question == "Is Alo Signature Corn Flake Crusted French Toast the dish shown in the image?" 
    assert food.image_path == "Toast"

