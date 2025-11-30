from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.CharField(max_length=200)
    receiver = models.CharField(max_length=200)
    content = models.TextField(null=False, blank=False)
    edited = models.BooleanField(editable=False, default=False)
    timestamp = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

class MessageHistory(models.Model):
    sender = models.CharField(max_length=200)
    receiver = models.CharField(max_length=200)
    content = models.TextField(null=False, blank=False)
    edited = models.BooleanField(editable=False, default=False)
    timestamp = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
