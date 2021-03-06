from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['fullName', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_username, email_provider = email.split("@")
        domain, extension = email_provider.split(".")
        if not extension == "edu":
            raise forms.ValidationError("Please use a valid .edu address")
        return email