from django.contrib import messages
from django.shortcuts import redirect


def guest_user(func, message="Page is not available"):

    def wrapper_func(request):
        if request.user.is_authenticated:
            messages.error(request, message)
            return redirect('/')
        else:
            return func(request)
    return wrapper_func
