from django.contrib.auth.forms import AuthenticationForm
from django import forms

# If you don't do this you cannot use Bootstrap CSS
class UserForm(forms.Form):
    username = forms.CharField(label="username", max_length=30,
                               required=True)
    password = forms.CharField(label="password", max_length=30,
                               widget=forms.PasswordInput, required=True)
    email = forms.EmailField(label = "email", max_length=30, required=True)