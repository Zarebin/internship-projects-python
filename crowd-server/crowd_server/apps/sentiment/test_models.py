from urllib import response
from venv import create

import pytest

from .models import Question, EvaluatedSentiment


def test_question_create():

    question = Question.objects.create(
    language = "en",
    question = "What kind of emotion is expressed in the text below?"
    )
    assert question.language == "en"
    assert question.question == "What kind of emotion is expressed in the text below?"
    


def test_evaluatedsentiment_create():
    evaluatedsentiment = EvaluatedSentiment.objects.create(
    answer_choice = "Positive"
    )
    assert evaluatedsentiment.answer_choice == "Positive"
    