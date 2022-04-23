from django import forms
from django.forms import ModelForm

from .models import Profile

class ProfileFOrm(ModelForm):
    class Meta:
        model = Profile
        fields=('first_name', 'last_name', 'email','about', 'background',)