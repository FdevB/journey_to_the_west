from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class ProfileModel(models.Model):
    """
    Model definition for ProfileModel.

    Extends the default User model with additional profile information.
    Each User has a one-to-one relationship with ProfileModel

    Attributes:
        user (OneToOneField to User): Owner of this profile.
        role (CharField): role of the user (*reader or critic or writer).
        avatar (ImageField, optional): Avatar of the user's profile.
        information (CharField, optional): Short information of the user.
        birth_day (DateField, optional): User's date of birth.
        phone (PhoneNumberField, optional): User's phone number.
        website (URLField, optional): User's website url.
        github (CharField, optional): User's GitHub username.

    Variables:
        ROLE_CHOICES (list[tuple(str, str)]): Available choices for user role.

    Note:
        This model uses `phonenumber_field` module for the phone field for convenience. You can use `CharField` and your validators.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    ROLE_CHOICES = [
        ('reader', 'Reader'),
        ('critic', 'Critic'),
        ('writer', 'Writer'),
    ]
    role = models.CharField(max_length=6, choices=ROLE_CHOICES, blank=True, default='reader')

    avatar = models.ImageField(upload_to='accounts/avatars/', default='accounts/avatars/default_avatar.jpg', blank=True)
    information = models.CharField(max_length=100, blank=True, null=True)
    birth_day = models.DateField(blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)

    website = models.URLField(blank=True, null=True)
    github = models.CharField(max_length=50, blank=True, null=True)


    class Meta:
        verbose_name = 'Profile'

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        """
        Returns the absolute URL for the profile view of this object.

        The URL is resolved using Django's reverse function based on the
        view name and the object's username.
        """

        return reverse('accounts_app:profile', kwargs={'username': self.user.username})

    @property
    def average_score(self):
        """
        Returns the average score of the user from the GradeModel.
        """

        return GradeModel.objects.filter(target_profile=self).aggregate(avg=models.Avg('score'))['avg'] or 0


class GradeModel(models.Model):
    """
    Model definition for GradeModel.

    Represents a rating that one User (grader) gives to another User (via target_profile).
    Multiple users can grade multiple profiles (many-to-many via GradeModel).
    The combination of grader and target_profile is unique.

    Attributes:
        grader (ForeignKey to User): User who gives the rating.
        target_profile (ForeignKey to ProfileModel): Profile of the user being rated.
        score (IntegerField): Score given by user | 0 <= score <= 5.
    """

    grader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='grades')
    target_profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='my_grades')

    score = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])


    class Meta:
        verbose_name = 'Grade'
        unique_together = [['grader', 'target_profile']]

    def __str__(self):
        return f"{self.grader} --> {self.target_profile} ({self.score})"
