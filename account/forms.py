from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# To set email field unique
User._meta.get_field('email')._unique = True

class CustomSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email':'Email'}