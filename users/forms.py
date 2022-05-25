from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#form for the user regisration
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # Meta - create configurations and keep them in 1 name
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#form for an exist user:
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

#profile update form:
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']