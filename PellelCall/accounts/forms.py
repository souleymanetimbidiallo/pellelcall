from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from meeting.models import Profile

class SignupForm(UserCreationForm):
    birthdate = forms.DateField(help_text='Obligatoire. Format: AAAA-MM-JJ', label="Date de naissance")
    class Meta:
        model = User
        fields = ('username', 'email', 'birthdate', 'password1', 'password2', )

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', );

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('birthdate', 'address', 'avatar') 