"""banka1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from healthclinicapp import views as healthclinic_views
from accounts import views as accounts_views

# Putanje u aplikaciji
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', healthclinic_views.home),
    path('', include("django.contrib.auth.urls")),
    path('show', include("django.contrib.auth.urls")),
    path('add', healthclinic_views.addScheduling),
    path('loggedoutadd', healthclinic_views.addSchedulingLoggedout),
    path('adddoctor', healthclinic_views.addDoctor),
    path('addpatient', healthclinic_views.addPatient),
    path('show', healthclinic_views.showScheduling),
    path('showdoctors', healthclinic_views.showDoctor),
    path('showpatients', healthclinic_views.showPatient),
    path('update/<int:id>', healthclinic_views.editScheduling, name="update"),
    path('loggedoutupdate/<int:id>',
         healthclinic_views.editSchedulingLoggedout, name="loggedoutupdate"),
    path('updatedoctor/<int:id>',
         healthclinic_views.editDoctor, name="updatedoctor"),
    path('updatepatient/<int:id>',
         healthclinic_views.editPatient, name="updatepatient"),
    path('updateloggedoutpatient/<int:id>',
         healthclinic_views.editPatientLoggedout, name="updateloggedoutpatient"),
    path('delete/<int:id>', healthclinic_views.deleteScheduling, name="delete"),
    path('loggedoutdelete/<int:id>',
         healthclinic_views.deleteSchedulingLoggedout, name="loggedoutdelete"),
    path('deletedoctor/<int:id>',
         healthclinic_views.deleteDoctor, name="deletedoctor"),
    path('deletepatient/<int:id>',
         healthclinic_views.deletePatient, name="deletepatient"),
    path('deleteloggedoutpatient/<int:id>',
         healthclinic_views.deletePatientLoggedout, name="deleteloggedoutpatient"),
    path('search', healthclinic_views.searchScheduling),
    path('login/', accounts_views.login_request),
    path('logout/', accounts_views.logout_user),
]
