import imp
from django.contrib import admin
from .models import Message, room

# Register your models here.

admin.site.register(room)
admin.site.register(Message)