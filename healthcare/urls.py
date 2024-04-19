from django.contrib import admin
from django.urls import path
from health import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf.urls.static import static
from django.conf import settings

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
    path('book-appointment/',views.book_appointment,name='book-appointment'),
    path('patient-prescription/', views.patient_prescription, name='patient-prescription'),
    path('medical-records',views.patient_medical_records),
    path('patient-settings/', views.patient_settings, name='patient_settings'),
    path('patient-settings/change-password/', views.patient_change_password, name='patient_change_password'),
    path('lab-results',views.lab_results,name='lab-results'),
    
    path('manage-appointments/', views.manage_appointments, name='manage-appointments'),
    path('accept-appointment/<int:appointment_id>/', views.accept_appointment, name='accept-appointment'),
    path('reject-appointment/<int:appointment_id>/', views.reject_appointment, name='reject-appointment'),
    path('admin-manage-appointments',views.admin_manage_appointments),
    path('admin-manage-patients',views.manage_patients,name='admin-manage-patients'),
    path('admin-manage-doctors',views.manage_doctors,name='admin-manage-doctors'),
    path('admin_settings/', views.admin_settings,name='admin_settings'),
    path('admin-settings/change-password/', views.change_password, name='change_password'),

    path('doctor-settings/', views.doctor_settings, name='doctor_settings'),
    path('doctor-manage-patients',views.doc_manage_patients,name='doctor-manage-patients'),
    path('doctor-settings/change-password/', views.doctor_change_password, name='doctor_change_password'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)