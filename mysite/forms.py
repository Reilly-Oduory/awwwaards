from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile, Project, Review, User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Enter Username"}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Enter Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': "Enter Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': "Confirm Password"}))


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
    
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"Fullname"}))
    profile_pic = forms.ImageField.widget.attrs={'class':"form-control"}
    d_o_b = forms.DateField(widget=forms.DateInput(attrs={'class':"form-control", 'placeholder':"Your Date of Birth"}))


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'd_o_b']

    fullname = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"Fullname"}))
    profile_pic = forms.ImageField.widget.attrs={'class':"form-control"}


class CreateProject(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user']

    project_pic = forms.ImageField.widget.attrs={'class':"form-control"}
    description = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control", 'placeholder':"Project Description"}))
    url = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"Project Url"}))



class UJpdateProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['description', 'url']

    description = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control", 'placeholder':"Project Description"}))
    url = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"Project Url"}))



class ReviewProject(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['user', 'project']