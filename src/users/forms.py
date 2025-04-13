# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import LibraryUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = LibraryUser
        fields = ('username', 'email', 'bio', 'profile_image', 'favorite_categories')
