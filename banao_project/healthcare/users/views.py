



from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from .forms import UserRegisterForm, PatientForm, DoctorForm
from .models import Patient, Doctor

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        patient_form = PatientForm(request.POST, request.FILES)
        doctor_form = DoctorForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()
            if user.is_patient and patient_form.is_valid():
                patient = Patient(user=user, **patient_form.cleaned_data)
                patient.save()
            elif user.is_doctor and doctor_form.is_valid():
                doctor = Doctor(user=user, **doctor_form.cleaned_data)
                doctor.save()
            
            # Specify the authentication backend
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
        patient_form = PatientForm()
        doctor_form = DoctorForm()
    
    return render(request, 'users/register.html', {
        'form': form,
        'patient_form': patient_form,
        'doctor_form': doctor_form
    })


def dashboard(request):
    user = request.user
    context = {}
    if user.is_patient:
        patient = Patient.objects.get(user=user)
        context['patient'] = patient
    elif user.is_doctor:
        doctor = Doctor.objects.get(user=user)
        context['doctor'] = doctor
    return render(request, 'users/dashboard.html', context)
