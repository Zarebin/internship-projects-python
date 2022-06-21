from urllib import response
from venv import create

import pytest

from .models import CompareQuestion, Comparison


def test_compare_question_create():

    compare_question = CompareQuestion.objects.create(
    language = "en",
    question = "Which dish is cheesier ; Coke Float (top) or Classic Hummus (bottom)?"
    )
    assert compare_question.language == "en"
    assert compare_question.question == "Which dish is cheesier ; Coke Float (top) or Classic Hummus (bottom)?"
    


def test_comparison():
    comparison = Comparison.objects.create(
    response = "Top"
    )
    assert comparison.response == "Top"
    
