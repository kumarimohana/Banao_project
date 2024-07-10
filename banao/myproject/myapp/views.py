# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import UserRegistrationForm

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        user = self.request.user
        if user.user_type == 'patient':
            return reverse_lazy('patient_dashboard')
        elif user.user_type == 'doctor':
            return reverse_lazy('doctor_dashboard')
        else:
            return reverse_lazy('login')  # Default fallback

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            if user.user_type == 'patient':
                return redirect('patient_dashboard')
            elif user.user_type == 'doctor':
                return redirect('doctor_dashboard')
            else:
                # Handle other user types if needed
                pass
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')

def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html')
