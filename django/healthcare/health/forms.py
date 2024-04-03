from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Doctor

class DoctorLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(DoctorLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Username"
        self.fields['password'].label = "Password"

class DoctorRegistrationForm(UserCreationForm):
    class Meta:
        model = Doctor
        fields = ['username', 'password']