from django.contrib import admin
from .models import Profile


# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user','first_name','last_name','bio',
                    'profile_img_preview','birthday','gender')


admin.site.register(Profile,ProfileAdmin)