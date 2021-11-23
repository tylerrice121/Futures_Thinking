from django.contrib import admin
from .models import UserEntries, AllEntries

# Register your models here.

admin.site.register(UserEntries)
admin.site.register(AllEntries)
