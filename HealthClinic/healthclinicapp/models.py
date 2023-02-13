from django.db import models


class TypeOfService(models.Model):
    ServiceName = models.CharField(max_length=30, null=False, blank=False)
    ServiceId = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.ServiceName

    class Meta:
        db_table = 'healthclinic_typeofservice'


class Doctor(models.Model):
    DoctorFirstName = models.CharField(max_length=30, null=False, blank=False)
    DoctorLastName = models.CharField(max_length=30, null=False, blank=False)
    DoctorPhoneNumber = models.CharField(
        max_length=30, null=False, blank=False, unique=True)
    DoctorType = models.ForeignKey(
        TypeOfService, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.DoctorFirstName + " " + self.DoctorLastName + ", " + str(self.DoctorType)

    class Meta:
        db_table = 'healthclinic_doctor'


class SchedulingLoggedout(models.Model):
    lPatientFirstName = models.CharField(
        max_length=30, null=False, blank=False)
    lPatientLastName = models.CharField(max_length=30, null=False, blank=False)
    lPatientJMBG = models.IntegerField(null=False, blank=False, unique=True)
    lPatientAddress = models.CharField(max_length=30, null=False, blank=False)
    lPatientPhoneNumber = models.CharField(
        max_length=30, null=False, blank=False)
    lScheduleName = models.CharField(max_length=30, null=False, blank=False)
    lScheduleType = models.ForeignKey(
        TypeOfService, null=False, blank=False, on_delete=models.CASCADE)
    lScheduleDoctor = models.ForeignKey(
        Doctor, null=False, blank=False, on_delete=models.CASCADE)
    lScheduleDateAndTime = models.DateTimeField(
        null=False, blank=False, unique=True)


class Patient(models.Model):
    PatientFirstName = models.CharField(max_length=30, null=False, blank=False)
    PatientLastName = models.CharField(max_length=30, null=False, blank=False)
    PatientJMBG = models.IntegerField(null=False, blank=False, unique=True)
    PatientAddress = models.CharField(max_length=30, null=False, blank=False)
    PatientPhoneNumber = models.CharField(
        max_length=30, null=False, blank=False)
    PatientLoggedout = models.ForeignKey(
        SchedulingLoggedout, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.PatientFirstName + " " + self.PatientLastName

    class Meta:
        db_table = 'healthclinic_patient'


class Scheduling(models.Model):
    ScheduleName = models.CharField(max_length=30, null=False, blank=False)
    ScheduleType = models.ForeignKey(
        TypeOfService, null=False, blank=False, on_delete=models.CASCADE)
    ScheduleDoctor = models.ForeignKey(
        Doctor, null=False, blank=False, on_delete=models.CASCADE)
    SchedulePatient = models.ForeignKey(
        Patient, null=False, blank=False, on_delete=models.CASCADE)
    ScheduleDateAndTime = models.DateTimeField(
        null=False, blank=False, unique=True)
    ScheduleLoggedout = models.ForeignKey(
        SchedulingLoggedout, null=True, blank=True, on_delete=models.CASCADE)
