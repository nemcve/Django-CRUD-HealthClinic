from django import forms
from .models import Doctor, Patient, Scheduling, SchedulingLoggedout


class SchedulingForm(forms.ModelForm):
    class Meta:
        model = Scheduling
        fields = ['ScheduleName', 'ScheduleType',
                  'ScheduleDoctor', 'SchedulePatient', 'ScheduleDateAndTime']
        ScheduleDateAndTime = forms.DateTimeField(
            input_formats=['%d/%m/%Y %H:%M'], widget=forms.DateTimeInput(format='%d/%m/%Y %H:%M'))
        labels = {
            "ScheduleName": "Scheduling reason ",
            "ScheduleType": "Appointment type ",
            "ScheduleDoctor": "Doctor ",
            "SchedulePatient": "Patient ",
            "ScheduleDateAndTime": "Date and time (month/day/year hour:minutes) ",
        }


class SchedulingLoggedoutForm(forms.ModelForm):
    class Meta:
        model = SchedulingLoggedout
        fields = "__all__"
        nZakazanoVremeiDatum = forms.DateTimeField(
            input_formats=['%d/%m/%Y %H:%M'], widget=forms.DateTimeInput(format='%d/%m/%Y %H:%M'))
        labels = {
            "lPatientFirstName": "First name ",
            "lPatientLastName": "Last name",
            "lPatientJMBG": "JMBG",
            "lPatientAddress": "Address",
            "lPatientPhoneNumber": "Phone number",
            "lScheduleName": "Scheduling reason ",
            "lScheduleType": "Scheduling type ",
            "lScheduleDoctor": "Doctor ",
            "lScheduleDateAndTime": "Date and time (month/day/year hour:minutes) ",
        }


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"
        labels = {
            "DoctorFirstName": "First name ",
            "DoctorLastName": "Last name ",
            "DoctorPhoneNumber": "Phone number ",
            "DoctorType": "Specialization ",
        }


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['PatientFirstName', 'PatientLastName',
                  'PatientJMBG', 'PatientAddress', 'PatientPhoneNumber']
        labels = {
            "PatientFirstName": "First name  ",
            "PatientLastName": "Last name ",
            "PatientJMBG": "JMBG ",
            "PatientAddress": "Address ",
            "PatientPhoneNumber": "Phone number ",
        }


class PatientLoggedoutForm(forms.ModelForm):
    class Meta:
        model = SchedulingLoggedout
        fields = ['lPatientFirstName', 'lPatientLastName',
                  'lPatientJMBG', 'lPatientAddress', 'lPatientPhoneNumber']
        labels = {
            "lPatientFirstName": "First name ",
            "lPatientLastName": "Last name ",
            "lPatientJMBG": "JMBG ",
            "lPatientAddress": "Address ",
            "lPatientPhoneNumber": "Phone number ",
        }
