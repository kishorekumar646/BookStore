from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):

    phone_number = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'placeholder': 'Enter a valid phone number', 'class': 'mb-4'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter a password', 'class': 'mb-4'}))

    def clean(self):
        super(LoginForm, self).clean()
        print("Clean")

        phone_number = self.cleaned_data.get('phone_number')
        password = self.cleaned_data.get('password')
        print(phone_number)

        return self.cleaned_data


class RegisterForm(forms.ModelForm):

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter a confirm password'}))
    class Meta:
        model = User
        fields = ['phone_number','password','email']
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter a password', 'class': 'mb-4'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter a valid phone number', 'class': 'mb-4'}),
        }
