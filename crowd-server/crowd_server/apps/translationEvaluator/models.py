from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Question(models.Model):
    question_text = models.TextField()
    answer_text = models.TextField()
    language = models.CharField(max_length=20)
    number_of_sent_answers = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.question_text#,self.answer_text


previous = "previous"
Skip ="skip"
true="true"
false="false"
ANSWER_CHOICES = (
    (previous, "previous"),
    (Skip, "skip"),
    (true, "true"),
    (false, "false")
)


class EvaluatedTranslation(models.Model):
    question = models.ForeignKey(Question, related_name='evaluated_translation', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='evaluated_translation', on_delete=models.CASCADE)
    value = models.CharField(max_length=10 , choices=ANSWER_CHOICES)


