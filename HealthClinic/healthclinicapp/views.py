# Create your views here.
from django.contrib import messages
from unicodedata import name
from django.shortcuts import render
from .models import Scheduling, Doctor, Patient, SchedulingLoggedout
from .forms import SchedulingForm, DoctorForm, PatientForm, SchedulingLoggedoutForm, PatientLoggedoutForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Function for rendering application homepage


def home(request):
    return render(request, "home.html")

# Function for scheduling by staff using form SchedulingForm defined in forms.py
# Function is visible and available just for staff users


@staff_member_required(login_url='login')
def addScheduling(request):
    # Defining that the form that is required in this case is SchedulingForm, and storing it in the "form" variable
    form = SchedulingForm()
    # Checking if request is POST type, if yes, the data is gathered from the form
    if request.method == 'POST':
        form = SchedulingForm(request.POST)
        # Validating form data (checking the type of inserted data,size,length,uniqueness, if null, checking that field isn't empty)
        if form.is_valid():
            # If the form passes validation and the data is saved, the application redirects the user to a page that contains all scheduled appointments via the urls.py path. (show.html)
            form.save()
            return redirect('/show')
        else:
            # Otherwise, the form shows an error
            messages.info(request, "The entered information is incorrect.")
    # Rendering form in the HTML document index.html
    context = {'form': form}
    return render(request, 'index.html', context)

# Function for scheduling appointments by the logged-out user


def addSchedulingLoggedout(request):
    form = SchedulingLoggedoutForm()
    if request.method == 'POST':
        form = SchedulingLoggedoutForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Appointment scheduled successfully.")
            return redirect('/')
        else:
            messages.info(request, "The entered information is incorrect.")
    context = {'form': form}
    return render(request, 'loggedoutindex.html', context)

# Function for adding the doctors by staff user using form "DoctorForm" defined in forms.py file


@staff_member_required(login_url='login')
def addDoctor(request):
    form = DoctorForm()
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/showdoctors')
        else:
            messages.info(request, "The entered information is incorrect.")
    context = {'form': form}
    return render(request, 'indexdoctor.html', context)

# Function for adding a patient by an employee via the PatientForm form defined in forms.py


@staff_member_required(login_url='login')
def addPatient(request):
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/showpatients')
        else:
            messages.info(request, "The entered information is incorrect.")
    context = {'form': form}
    return render(request, 'indexpatient.html', context)

# A function to display all scheduled appointments that is only available to the staff user


@staff_member_required(login_url='login')
def showScheduling(request):
    # storing all appointments from the Scheduling class into the scheduling variable
    # storing all appointments from the SchedulingLoggedout class into the schedulingloggedout variable
    scheduling = Scheduling.objects.all
    schedulingloggedout = SchedulingLoggedout.objects.all
    # rendering variables in the page for displaying all appointments in which they are called via a for loop
    return render(request, 'show.html', {'scheduling': scheduling, 'schedulingloggedout': schedulingloggedout})

# Function to display all doctors available to staff and users who are not logged in


def showDoctor(request):
    doctor = Doctor.objects.all
    return render(request, 'showdoctors.html', {'doctor': doctor})

# A function to display all patients that is only available to the staff user


@staff_member_required(login_url='login')
def showPatient(request):
    patient = Patient.objects.all
    patientloggedout = SchedulingLoggedout.objects.all
    return render(request, 'showpatients.html', {'patient': patient, 'patientloggedout': patientloggedout})

# Function to edit patients which is available only to the staff user


@staff_member_required(login_url='login')
def editScheduling(request, id):
    # The data for the selected appointment is taken from the Scheduling class by ID
    scheduling = Scheduling.objects.get(id=id)
    # The data is stored inside the form in the corresponding fields
    form = SchedulingForm(instance=scheduling)
    if request.method == 'POST':
        # A form with data from the selected instance of the Scheduling class is displayed
        form = SchedulingForm(request.POST, instance=scheduling)
        if form.is_valid():
            form.save()
            return redirect('/show')
    context = {'form': form}
    return render(request, 'index.html', context)

# A function for editing scheduled appointments by a non-registered user that is only available to the staff user


@staff_member_required(login_url='login')
def editSchedulingLoggedout(request, id):
    schedulingloggedout = SchedulingLoggedout.objects.get(id=id)
    form = SchedulingLoggedoutForm(instance=schedulingloggedout)

    if request.method == 'POST':
        form = SchedulingLoggedoutForm(
            request.POST, instance=schedulingloggedout)
        if form.is_valid():
            form.save()
            return redirect('/show')
    context = {'form': form}
    return render(request, 'loggedoutindex.html', context)

# The function for editing Doctors is available only to the staff user


@staff_member_required(login_url='login')
def editDoctor(request, id):
    doctor = Doctor.objects.get(id=id)
    form = DoctorForm(instance=doctor)

    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('/showdoctors')
    context = {'form': form}
    return render(request, 'indexdoctor.html', context)

# The function for editing patients is available only to the staff user


@staff_member_required(login_url='login')
def editPatient(request, id):
    patient = Patient.objects.get(id=id)
    form = PatientForm(instance=patient)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('/showpatients')
    context = {'form': form}
    return render(request, 'indexpatient.html', context)

# The function for editing patients inserted by loggedout users is available only to the staff user


@staff_member_required(login_url='login')
def editPatientLoggedout(request, id):
    patientloggedout = SchedulingLoggedout.objects.get(id=id)
    form = PatientLoggedoutForm(instance=patientloggedout)

    if request.method == 'POST':
        form = PatientLoggedoutForm(
            request.POST, instance=patientloggedout)
        if form.is_valid():
            form.save()
            return redirect('/showpatients')
    context = {'form': form}
    return render(request, 'indexloggedoutpatient.html', context)

# A function to delete scheduled appointments that is only available to the staff user


@staff_member_required(login_url='login')
def deleteScheduling(request, id):
    scheduling = Scheduling.objects.get(id=id)
    scheduling.delete()
    return redirect('/show')

# A function for deleting scheduled appointments inserted by non-registered users that is only available to the staff user


@staff_member_required(login_url='login')
def deleteSchedulingLoggedout(request, id):
    schedulingloggedout = SchedulingLoggedout.objects.get(id=id)
    schedulingloggedout.delete()
    return redirect('/show')

# A function to delete inserted doctors that is only available to the staff user


@staff_member_required(login_url='login')
def deleteDoctor(request, id):
    doctor = Doctor.objects.get(id=id)
    doctor.delete()
    return redirect('/showdoctors')

# A function to delete inserted patients that is only available to the staff user


@staff_member_required(login_url='login')
def deletePatient(request, id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    return redirect('/showpatients')

# A function to delete patients inserted by non-registered users that is only available to the staff user


@staff_member_required(login_url='login')
def deletePatientLoggedout(request, id):
    patientloggedout = SchedulingLoggedout.objects.get(id=id)
    patientloggedout.delete()
    return redirect('/showpatients')

# A function to search for scheduled appointments by patients JMBG, which is only available to the staff user


@staff_member_required(login_url='login')
def searchScheduling(request):
    entered_jmbg = request.POST['name']
    scheduling = Scheduling.objects.filter(
        SchedulePatient__PatientJMBG__icontains=entered_jmbg)
    schedulingloggedout = SchedulingLoggedout.objects.filter(
        lPatientJMBG__icontains=entered_jmbg)
    return render(request, 'show.html', {'scheduling': scheduling, 'schedulingloggedout': schedulingloggedout})
