from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import password_validation

class UserForm(UserCreationForm):
    
    # class Meta:
    #     model = User
    #     fields = ('username', 'email', 'password1', 'password2')
    
    username = UsernameField(
        label=("Username"),
        widget=forms.TextInput(attrs={"autofocus": True,'class' : "rounded border border-warning shadow-lg mt-5", "placeHolder" :"username"})
        )
    
    password1 = forms.CharField(
        label=("Password"),
        widget=forms.PasswordInput(attrs={'class' : "rounded border border-warning shadow-lg", "placeHolder" :"password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    
    password2 = forms.CharField(
        label=("Password Confirmation"),
        widget=forms.PasswordInput(attrs={'class' : "rounded border border-warning shadow-lg", "placeHolder" :"password confirmation"}),
        help_text=("* Enter the same password as before, for verification."),
    )
    
class LoginForm(AuthenticationForm):
    username = UsernameField(
        label=("username"), 
        widget=forms.TextInput(attrs={"autofocus": True, 'class' : "rounded border border-warning form-control shadow-lg m-2", "placeHolder" :"username"}))
    password = forms.CharField(
        label=("password"),
        widget=forms.PasswordInput(attrs={'class' : "rounded border border-warning form-control shadow-lg m-2", "placeHolder" :"password"}),
    )
    
