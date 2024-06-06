from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.PasswordInput()

class SignUpForm(UserCreationForm):
  username = forms.CharField(
    widget= forms.TextInput(
      attrs={
        'placeholder': 'Give your username',
        'class': 'form-control',
      }
    )
  )
  email = forms.EmailField(
    widget=forms.EmailInput(
      attrs={
        'placeholder': 'Give your email',
        'class': 'form-control',
      }
    )
  )
  password1 = forms.CharField(
    widget=forms.PasswordInput(
      attrs={
        'placeholder': 'Give your password',
        'class': 'form-control',
      }
    )
  )
  password2 = forms.CharField(
    widget=forms.PasswordInput(
      attrs={
        'placeholder': 'Give your password',
        'class': 'form-control',
      }
    )
  )


  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')