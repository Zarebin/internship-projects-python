from django.contrib import admin

from .models import CustomUser, Question, Answer

admin.site.register(CustomUser)
admin.site.register(Question)
admin.site.register(Answer)
