from django import forms
from .models import UserGame
from django.contrib.auth.forms import AuthenticationForm


class UserChangeForm2(forms.ModelForm):
    class Meta:
        model = UserGame
        fields = ('username', 'password','email','first_name', 'last_name','image')
