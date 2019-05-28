from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    email = forms.EmailField(max_length=25, help_text='Required. Inform a valid email address.', widget=forms.TextInput(attrs={'class' : 'form-control'}))
    username = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class' : 'form-control'}))

    password1 = forms.CharField(help_text='Required.', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    password2 = forms.CharField(help_text='ConfirmPassword.', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password1')
