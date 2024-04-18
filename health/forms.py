from django import forms
from django.contrib.auth.models import User
from . import models
from . models import HealthData,Appointment,Prescription



#for admin signup
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }


#for student related form
class DoctorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class DoctorForm(forms.ModelForm):
    class Meta:
        model=models.Doctor
        fields=['address','mobile','department']


class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class PatientForm(forms.ModelForm):
    class Meta:
        model=models.Patient
        fields=['address','mobile','symptoms',]

class HealthDataForm(forms.ModelForm):
    class Meta:
        model = HealthData
        fields = ['blood_pressure', 'sugar_level', 'height', 'weight', 'bmi','body_temperature','heart_rate','cholestrol_level']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['prescription_file']



