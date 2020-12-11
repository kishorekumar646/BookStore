from django.shortcuts import render,redirect
from django.views import View
from .forms import LoginForm


class Login(View):

    def get(self, request):
        form = LoginForm()
        return render(request, "accounts/login.html",{'form': form})

    def post(self, request):
        print(request.POST)
        return redirect('home')


class Register(View):

    def get(self, request):

        return render(request, "accounts/register.html")


class Logout(View):

    def get(self, request):

        return render(request, "accounts/login.html")
