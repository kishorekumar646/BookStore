from django.shortcuts import render,redirect
from django.views import View


class Login(View):

    def get(self, request):

        return render(request, "accounts/login.html")

    def post(self, request):
        print(request.POST)
        return redirect('home')


class Register(View):

    def get(self, request):

        return render(request, "accounts/register.html")


class Logout(View):

    def get(self, request):

        return render(request, "accounts/login.html")
