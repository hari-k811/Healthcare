from django.shortcuts import render,redirect,reverse,get_object_or_404
from . import forms,models
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from django.conf import settings
from . forms import HealthDataForm,AppointmentForm,PrescriptionForm
from . models import HealthData,Appointment,Doctor,Patient,Prescription
from django.http import HttpResponseBadRequest

# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'index.html')

def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'adminclick.html')

def doctorclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'doctorclick.html')

def patientclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'patientclick.html')


def admin_signup_view(request):
    form=forms.AdminSigupForm()
    if request.method=='POST':
        form=forms.AdminSigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
            return HttpResponseRedirect('adminlogin')
    return render(request,'adminsignup.html',{'form':form})

def doctor_signup_view(request):
    userForm=forms.DoctorUserForm()
    doctorForm=forms.DoctorForm()
    mydict={'userForm':userForm,'doctorForm':doctorForm}
    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST)
        doctorForm=forms.DoctorForm(request.POST,request.FILES)
        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            doctor=doctorForm.save(commit=False)
            doctor.user=user
            doctor=doctor.save()
            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)
        return HttpResponseRedirect('doctorlogin')
    return render(request,'doctorsignup.html',context=mydict)

def patient_signup_view(request):
    userForm=forms.PatientUserForm()
    patientForm=forms.PatientForm()
    mydict={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST)
        patientForm=forms.PatientForm(request.POST,request.FILES)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            patient=patientForm.save(commit=False)
            patient.user=user
            patient=patient.save()
            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)
        return HttpResponseRedirect('patientlogin')
    return render(request,'patientsignup.html',context=mydict)


def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()
def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()


def afterlogin_view(request):
    error_message = None
    
    if is_admin(request.user):
        return redirect('admin-dashboard')
    elif is_doctor(request.user):
        return redirect('doctor-dashboard')
    elif is_patient(request.user):
        return redirect('patient-dashboard')
    else:
        error_message = "Invalid username or password. Please try again."

    return render(request, 'index.html', {'error_message': error_message})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_dashboard_view(request):
    appointments = Appointment.objects.all()
    return render(request, 'admin_dashboard.html', {'appointments': appointments})

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_dashboard_view(request):
    appointments = Appointment.objects.filter(doctor=request.user.doctor)
    return render(request, 'doctor_dashboard.html', {'appointments': appointments})

@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_dashboard_view(request):
    patient = request.user.patient
    health_data = HealthData.objects.filter(patient=patient)
    return render(request, 'patient_dashboard.html', {'health_data': health_data})


@login_required
def patientprofile_view(request):
    if request.method == 'POST':
        form = HealthDataForm(request.POST)
        if form.is_valid():
            health_data = form.save(commit=False)
            # Get the patient associated with the current user
            patient = request.user.patient
            health_data.patient = patient
            health_data.save()
            return redirect('patient-dashboard') 
    else:
        form = HealthDataForm()
    return render(request, 'patientprofile.html', {'form': form})

@login_required
def patient_details(request):
    patient = request.user.patient
    return render(request,'patirnt_details.html')

@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user.patient
            appointment.save()
            return redirect('patient-dashboard')
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form})

@login_required
def manage_appointments(request):
    doctor = request.user.doctor
    appointments = Appointment.objects.filter(doctor=doctor)
    return render(request, 'manage_appointments.html', {'appointments': appointments})

@login_required
def accept_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.accepted = True
    appointment.save()
    return redirect('manage-appointments')

@login_required
def reject_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.delete()
    return redirect('manage-appointments')

def admin_manage_appointments(request):
    return render(request,'admin_manage_appointments.html')

@login_required
def patient_prescription(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST, request.FILES)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.patient = request.user
            prescription.save()
            return redirect('patient-prescription')
    else:
        form = PrescriptionForm()
    
    prescriptions = Prescription.objects.filter(patient=request.user)
    return render(request, 'patient_prescription.html', {'form': form, 'prescriptions': prescriptions})

@login_required
def appointment_view(request):
    return render(request,'appointments.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def manage_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'admin_manage_doctors.html', {'doctors': doctors})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def manage_patients(request):
    patients = Patient.objects.all()
    return render(request, 'admin_manage_patients.html', {'patients': patients})