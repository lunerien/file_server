# files/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import File, CustomUser


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'file']


class CustomUserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')
