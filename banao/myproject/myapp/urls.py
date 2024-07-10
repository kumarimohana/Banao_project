# myproject/urls.py
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from myapp.views import CustomLoginView, register, patient_dashboard, doctor_dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('patient_dashboard/', patient_dashboard, name='patient_dashboard'),
    path('doctor_dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
