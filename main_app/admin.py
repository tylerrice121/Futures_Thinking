from django.contrib import admin
from .models import UserEntries, AllEntries, Comment, Profile
from embed_video.admin import AdminVideoMixin




class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

# Register your models here.

admin.site.register(UserEntries)
admin.site.register(AllEntries)
admin.site.register(Comment)
admin.site.register(Profile)

 




