from email.policy import default
from django.db import models
from datetime import datetime

# Create your models here.

class room(models.Model):
    room_name = models.CharField(max_length=100)

class Message(models.Model):
    value=models.CharField(max_length=100000)
    date=models.DateTimeField(default=datetime.now, blank=True)
    user=models.CharField(max_length=100000)
    room=models.CharField(max_length=100000)