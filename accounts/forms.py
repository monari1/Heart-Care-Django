from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)