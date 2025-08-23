from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    """
    SignupForm extends Django's built-in UserCreationForm to include an email field.

    Attributes:
        email (EmailField): The email address of the new user.
    """

    email = forms.EmailField()

    class Meta:
        model = User
        fields = UserCreationForm._meta.fields + ('email',)

    def save(self, commit=True):
        """
        Save the user instance with the provided email.

        Args:
            commit (bool): If True, save the user to the database immediately.
                           If False, return the user object without saving.

        Returns:
            User: The created user instance with the assigned email.
        """

        user = super().save(commit)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()

        return user
