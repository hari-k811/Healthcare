"""
URL configuration for healthcare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from health import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),

    path('adminclick/', views.adminclick_view),
    path('doctorclick/', views.doctorclick_view,name='doctorclick'),
    path('patientclick/', views.patientclick_view),

    path('adminsignup/', views.admin_signup_view),
    path('adminsignup/adminlogin', LoginView.as_view(template_name='adminlogin.html')),
    path('doctorsignup', views.doctor_signup_view,name='doctorsignup'),
    path('patientsignup/', views.patient_signup_view,name='patientsignup'),
    path('patientsignup/patientlogin',views.patientclick_view),
    
    path('adminlogin', LoginView.as_view(template_name='adminlogin.html')),
    path('doctorlogin', LoginView.as_view(template_name='doctorlogin.html')),
    path('patientlogin', LoginView.as_view(template_name='patientlogin.html')),


    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='index.html'),name='logout'),

    path('accounts/profile/',views.afterlogin_view,name='afterlogin'),

    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    path('doctor-dashboard',views.doctor_dashboard_view,name='doctor-dashboard'),
    path('patient-dashboard',views.patient_dashboard_view,name='patient-dashboard'),


    path('patientprofile', views.patientprofile_view,name='patientprofile'),
    path('patient_details/', views.patient_details, name='patient_details'),
    
    path('book-appointment/', views.book_appointment, name='book-appointment'),
    path('approve-appointment/<int:appointment_id>/', views.approve_appointment, name='approve-appointment'),
    path('reject-appointment/<int:appointment_id>/', views.reject_appointment, name='reject-appointment'),
    path('accept-reject-appointment/<int:appointment_id>/', views.accept_reject_appointment, name='accept-reject-appointment'),
    path('accept-reject-appointment/', views.appointment_view, name='accept-reject-appointment'),
    path('admin-manage-patients',views.manage_patients),
    path('admin-manage-doctors',views.manage_doctors),
]