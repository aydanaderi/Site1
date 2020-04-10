from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class SignUpForm(UserCreationForm):
    username = forms.IntegerField(min_value = 9000000000 ,max_value = 9999999999)
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    password1 = forms.CharField(max_length = 50,validators = [alphanumeric])
    password2 = forms.CharField(max_length = 50,validators = [alphanumeric])
