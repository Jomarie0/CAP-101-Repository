# from django import forms
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class CustomAuthenticationForm(AuthenticationForm):
    pass
