from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.views import View
from django.contrib import messages
from bookstore_backend import status
from .forms import LoginForm, RegisterForm


class Login(View):

    def get(self, request):
        print(request.user)
        if not request.user.is_authenticated:
            form = LoginForm()
            return render(request, "accounts/login.html", {'form': form})

        else:
            return redirect('home')

    def post(self, request):

        form = LoginForm(request.POST or None)
        print(form.errors)
        if request.POST and form.is_valid():
            user = form.login(request)
            if user:
                print(user)
                login(request, user)
                return redirect('home')

        else:
            return redirect('login')


class Register(View):

    def get(self, request):
        if not request.user.is_authenticated:
            form = RegisterForm()
            return render(request, "accounts/register.html", {'form': form})

        else:
            return redirect('home')

    def post(self, request):

        form = RegisterForm(request.POST)
        if form.is_valid():
            print(request.POST)
            user = form.save()
            user.save()
            messages.info(self.request, "Successfully registered")
            return redirect('login')
        else:
            return render(request, 'accounts/register.html', {'form': form}, status=status.HTTP_406_NOT_ACCEPTABLE)


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('login')
