from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from captcha.fields import CaptchaField

from accounts_app.models import GradeModel, ProfileModel


class SignupForm(UserCreationForm):
    """
    SignupForm extends Django's built-in UserCreationForm to include an email field.

    Attributes:
        captcha (CaptchaField): Ensures the form is submitted by a human.
    """

    captcha = CaptchaField()


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


class LoginForm(AuthenticationForm):
    """
    LoginForm extends Django's built-in AuthenticationForm to include an captcha field.

    Attributes:
        captcha (CaptchaField): Ensures the form is submitted by a human.
    """

    captcha = CaptchaField()


class ChangeUserDetailForm(forms.ModelForm):
    """
    A form for updating basic user information (first name, last name, email).
    Uses Django's built-in User model.

    Attributes:
        captcha (CaptchaField): Ensures the form is submitted by a human.
    """

    captcha = CaptchaField()


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ChangeUserProfileForm(forms.ModelForm):
    """
    A form for updating additional profile information from ProfileModel.
    Excludes the related 'user' field and customizes the 'birth_day' widget.
    """

    class Meta:
        model = ProfileModel
        exclude = ['user']

        widgets = {
            'birth_day': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }


class GradeForm(forms.ModelForm):

    class Meta:
        model = GradeModel
        fields = ['score']
