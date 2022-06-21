from django.contrib import admin

from .models import Question,CompareQuestion

admin.site.register(Question)
admin.site.register(CompareQuestion)