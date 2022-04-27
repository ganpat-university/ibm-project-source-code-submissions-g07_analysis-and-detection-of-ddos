from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.core.exceptions import ValidationError

def validate_email(value):
    if User.objects.filter(email = value).exists():
        raise ValidationError((f"{value} already exists !!!."),params = {'value':value})

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, validators = [validate_email])

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
