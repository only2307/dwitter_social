from django.contrib.auth.forms import UserCreationForm
from django import forms
from dwitter.models import Profile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65, 
                               required=True, 
                               error_messages = {'required':"Please Enter your Name"})
    password = forms.CharField(max_length=65, 
                               required=True, 
                               widget=forms.PasswordInput,
                               error_messages = {'required':"Please Enter your Password"})

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)