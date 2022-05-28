from rest_framework import serializers

from .models import Question
from .models import Answer


# Create a model serializer
class QuestionSerializer(serializers.HyperlinkedModelSerializer):
	# specify model and fields
	class Meta:
		model = Question
		fields = ('id', 'question', 'image_url', 'language')


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
	# specify model and fields
	class Meta:
		model = Answer
		fields = ('id', 'question_id', 'user_id', 'fact')
