from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Signupform(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm your password'}))

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2',)
        