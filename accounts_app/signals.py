from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts_app.models import ProfileModel


@receiver(post_save, sender=User)
def create_user_profile_signal(sender, instance, created, **kwargs):
    """
    Signal triggered after a new User is created.

    This signal ensures that a Profile instance is automatically created and linked to the User.

    Args:
        sender (Model): The model class that sent the signal (User).
        instance (User): The actual User instance created.
        created (bool): Indicates whether a new User was created.
        **kwargs: Additional keyword arguments.
    """

    if created:
        ProfileModel.objects.create(user=instance)
