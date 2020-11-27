from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.forms import PasswordInput


class UserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-input form-input-lg'
        self.fields['username'].widget.attrs['placeholder'] = 'Your Username'
        self.fields['email'].widget.attrs['class'] = 'form-input form-input-lg'
        self.fields['email'].widget.attrs['placeholder'] = 'Your Email'
        self.fields['email'].widget.attrs['name'] = 'email'
        self.fields['first_name'].widget.attrs['class'] = 'form-input form-input-lg'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Your Firstname'
        self.fields['first_name'].widget.attrs['name'] = 'first_name'
        self.fields['last_name'].widget.attrs['class'] = 'form-input form-input-lg'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Your Lastname'
        self.fields['last_name'].widget.attrs['name'] = 'last_name'
        self.fields['password1'].widget.attrs['class'] = 'form-input form-input-lg'
        self.fields['password1'].widget.attrs['id'] = 'password'
        self.fields['password1'].widget.attrs['name'] = 'password'
        self.fields['password1'].widget.attrs['placeholder'] = 'Your Password'
        self.fields['password1'].widget.attrs['data-toggle'] = 'password'
        self.fields['password2'].widget.attrs['class'] = 'form-input form-input-lg'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'
        self.fields['password2'].widget.attrs['name'] = 're_password'
        self.fields['password2'].widget.attrs['id'] = 're_password'

    class Meta:
        model = User
        fields = ['id','username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            "password": PasswordInput(attrs={'placeholder':'********','autocomplete': 'off','data-toggle': 'password'}),
        }
