from django import forms

from captcha.fields import CaptchaField

from info_app.models import MessageModel

# create your forms
class MessageForm(forms.ModelForm):
    """
    Form for collecting user messages.
    Includes a captcha field to prevent spam submissions.

    Attributes:
        captcha (CaptchaField): Ensures the form is submitted by a human.
    """

    captcha = CaptchaField()


    class Meta:
        model = MessageModel
        exclude = ['is_read', 'sent_at']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'common-input mb-20 form-control',
                'placeholder': 'Enter your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'common-input mb-20 form-control',
                'placeholder': 'Enter email address'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'common-input mb-20 form-control',
                'placeholder': 'Enter Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'common-textarea form-control',
                'placeholder': 'Enter Message'
            })
        }
