from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, ProfileForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def register_request(request):
    form = RegistrationForm()
    profile_form = ProfileForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, "Profile is successfully created!")
            return redirect('/login')
        else:
            form = RegistrationForm()
            profil_form = ProfileForm()
    context = {"register_form": form, "profile_form": profile_form}
    return render(request, "registration/register.html", context)

def login_request(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Wrong username or password.")
    else:
        context = {}
        return render(request, "registration/login.html", context)
    
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    return render(request, "registration/profile.html")
