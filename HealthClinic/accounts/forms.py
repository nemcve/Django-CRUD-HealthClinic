from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserProfile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label='E-mail', widget=forms.EmailInput, required=True)

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Username"
        self.fields['first_name'].label = "First name"
        self.fields['last_name'].label = "Last name"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Repeat password"

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['JMBG'].label = "JMBG"

    class Meta:
        model = UserProfile
        fields = ["JMBG"]
