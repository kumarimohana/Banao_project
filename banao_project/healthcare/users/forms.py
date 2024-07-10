from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Patient, Doctor

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_patient', 'is_doctor']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'profile_picture', 'address_line1', 'city', 'state', 'pincode']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'profile_picture', 'address_line1', 'city', 'state', 'pincode']
