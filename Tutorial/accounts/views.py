from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

def home(request):
    numbers = [1,2,3,4,5]
    name = 'Max Goodridge'

    args = {'myName': name, 'numbers': numbers}
    return render(request, 'account/home.html', args)

def register(request):
    if request.method == 'POST':
        # form = RegistrationForm(request.POST)
        if RegistrationForm(request.POST).is_valid():
            RegistrationForm(request.POST).save()
            return redirect('/account')
    else:
        # form = RegistrationForm()

        # args = {'form': RegistrationForm()}
        return render(request, 'account/reg_form.html', {'form': RegistrationForm})

def view_profile(request):
    args = {"user": request.user}
    return render(request, 'account/profile.html', args)
def edit_profile(request):
    if request.method == "POST":   
        form = UserChangeForm(request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    else:
        form = UserChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, 'account/edit_profile.html', args)

