from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from .forms import LoginForm


class Login(View):

    def get(self, request):
        form = LoginForm()
        return render(request, "accounts/login.html",{'form': form})

    def post(self, request):
        
        form = LoginForm(request.POST)
        if form.is_valid():
            print(request.POST)

            return redirect('home')
        else:
            return render(request, "accounts/login.html",{'form': form})


class Register(View):

    def get(self, request):

        return render(request, "accounts/register.html")


class Logout(View):

    def get(self, request):

        return render(request, "accounts/login.html")
