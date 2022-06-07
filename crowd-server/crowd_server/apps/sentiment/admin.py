from django.contrib import admin

from .models import Question,EvaluatedSentiment

admin.site.register(Question)
admin.site.register(EvaluatedSentiment)