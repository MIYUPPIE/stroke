from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver
from .models import Activity

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    if user:
        Activity.objects.create(user=user, action="Logged out")