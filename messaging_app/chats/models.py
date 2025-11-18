from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICE = (
        ('guest', 'Guest'),
        ('host', 'Host'),
        ('admin', 'Admin'),
    )

    user_id = models.UUIDField()
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False, unique=True)
    password_hash = models.CharField(max_length=100, null=False)
    phone_number = models.CharField(max_length=100, null=True)
    role = models.Choices=ROLE_CHOICE
    created_at = models.DateField(auto_now=True)

class Message(models.Model):
    message_id = models.UUIDField()
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE)
    message_body = models.TextField(null=False)
    sent_at = models.DateField(auto_now=True)

class Conversation(models.Model):
    conversation_id = models.UUIDField()
    participants_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)
