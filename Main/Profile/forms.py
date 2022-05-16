from django import forms
from django.forms import ModelForm

from .models import Profile

from Post.models import Rewards

class ProfileFOrm(ModelForm):
    class Meta:
        model = Profile
        fields=('first_name', 'last_name', 'email','about', 'background',)
        
class RewardForm(ModelForm):
    class Meta:
        model=Rewards
        fields=('reward',)