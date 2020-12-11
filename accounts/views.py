from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from .forms import LoginForm, RegisterForm


class Login(View):

    def get(self, request):
        form = LoginForm()
        return render(request, "accounts/login.html", {'form': form})

    def post(self, request):

        form = LoginForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print(request.POST)
            return redirect('home')
        else:
            return render(request, "accounts/login.html", {'form': form})


class Register(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, "accounts/register.html",{'form': form})

    def post(self, request):

        form = RegisterForm(request.POST)
        print(form.errors)
        print(form.is_valid())
        if form.is_valid():
            print(request.POST)

            return redirect('login')
        else:
            return render(request, "accounts/register.html", {'form': form})


class Logout(View):

    def get(self, request):

        return render(request, "accounts/login.html")
