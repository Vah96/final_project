from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegisterForm
# from django.core.mail import BadHeaderError, send_mail
# from django.http import HttpResponse, HttpResponseRedirect


def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']

            user = register_form.save()
            login(request, user)
            messages.success(request, f'Hi "{username}", you have successfully registered!!!')
            return redirect('/')
    else:
        register_form = RegisterForm()
    return render(request, 'register.html', {'form': register_form})
