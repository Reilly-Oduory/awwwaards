from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, fields
from .models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Enter Username"}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Enter Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': "Enter Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': "Confirm Password"}))