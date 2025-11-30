from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Message, Notification

@receiver(post_save, sender=Message)
def trigger_notification_upon_new_message(instance, sender, created, **kwargs):
    if not created:
        return
    
    if created:
        # sender = instance.sender
        # message = instance.content
        # notification = f"New message from {sender}. {message}"

        Notification.save(user=instance.sender, message=instance)