from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = UserCreationForm._meta.fields + ('email',)

    def save(self, commit=True):
        user = super().save(commit)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()

        return user
