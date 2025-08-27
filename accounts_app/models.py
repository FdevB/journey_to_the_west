from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    avatar = models.ImageField(upload_to='accounts/avatars/', default='accounts/avatars/default_avatar.jpg', blank=True)
    phone = PhoneNumberField(blank=True)

    website = models.URLField(blank=True, null=True)
    github = models.CharField(max_length=50, blank=True, null=True)

    # RULE
    birth_day = models.DateField(blank=True, null=True)
    # POINT
    information = models.CharField(max_length=100, blank=True, null=True)
    # POST_COUNTS

    class Meta:
        verbose_name = 'Profile'

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('accounts_app:profile', kwargs={'username': self.user.username})
