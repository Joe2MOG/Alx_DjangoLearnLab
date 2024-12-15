from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = get_user_model()

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")  # User receiving the notification
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications_from")  # User performing the action
    verb = models.CharField(max_length=255)  # Description of the action
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    target_object_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey('target_content_type', 'target_object_id')  # The object associated with the action
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp for when the notification was created

    def __str__(self):
        return f"Notification to {self.recipient} - {self.verb}"
