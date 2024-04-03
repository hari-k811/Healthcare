from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import DoctorLoginForm
from .models import Doctor

# Create your views here.
def home(request):
    return render(request,'index.html')

def doctor_login(request):
    return render(request,'doctor_login.html')

# def doctor_dashboard(request):
#     return render(request,'doctor_dashboard.html')

def doctor_login_page(request):
    if request.method == 'POST':
        form = DoctorLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page
                return redirect('success_page')
            else:
                # Handle invalid login
                return render(request, 'doctor_login.html', {'form': form, 'error_message': 'Invalid credentials'})
    else:
        form = DoctorLoginForm()
    return render(request, 'doctor_login.html', {'form': form})

def doctor_register(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Redirect to a success page
            return redirect('success_page')
    else:
        form = DoctorRegistrationForm()
    return render(request, 'doctor_register.html', {'form': form})
