from django.shortcuts import render, redirect
from .forms import RegistrationForm


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