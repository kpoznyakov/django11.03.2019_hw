# from .models import AccountUser
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import LoginForm


# Create your views here.

def register(request):
    pass


def login_view(request):
    form = LoginForm

    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(
                username=username,
                password=password,
            )

            if user and user.is_active:
                login(request, user)
                return redirect('main:main')

    return render(
        request,
        'authentication/login.html',
        {'form': form}
    )
