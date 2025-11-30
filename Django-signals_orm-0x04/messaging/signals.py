from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from .models import Message, Notification, MessageHistory

@receiver(post_save, sender=Message)
def trigger_notification_upon_new_message(instance, sender, created, **kwargs):
    if not created:
        return
    
    if created:
        Notification.objects.create(user=instance.sender, message=instance)

@receiver(pre_save, sender=Message)
def save_message_history(instance, sender, updated, **kwargs):
    if not updated:
        return
    
    if updated:
        MessageHistory.objects.create(sender =instance.sender, receiver=instance.receiver ,content=instance.content, edited_by=instance.sender)