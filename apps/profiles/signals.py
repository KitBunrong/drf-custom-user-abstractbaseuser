"""
We create 'signals.py' to ensure that user `profile` is created
whenever new user instance is created.
"""
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.profiles.models import Profile
from config.settings import AUTH_USER_MODEL

@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()