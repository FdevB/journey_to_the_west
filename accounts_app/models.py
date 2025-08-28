from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    avatar = models.ImageField(upload_to='accounts/avatars/', default='accounts/avatars/default_avatar.jpg', blank=True)
    information = models.CharField(max_length=100, blank=True, null=True)
    birth_day = models.DateField(blank=True, null=True)
    phone = PhoneNumberField(blank=True)

    website = models.URLField(blank=True, null=True)
    github = models.CharField(max_length=50, blank=True, null=True)


    class Meta:
        verbose_name = 'Profile'

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('accounts_app:profile', kwargs={'username': self.user.username})

    @property
    def average_score(self):
        return GradeModel.objects.filter(target_profile=self).aggregate(avg=models.Avg('score'))['avg'] or 0


class GradeModel(models.Model):
    grader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='grades')
    target_profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='my_grades')
    score = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])


    class Meta:
        verbose_name = 'Grade'
        unique_together = [['grader', 'target_profile']]

    def __str__(self):
        return f"{self.grader} --> {self.target_profile} ({self.score})"
