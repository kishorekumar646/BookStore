from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class LoginForm(forms.Form):
    phone_regex = RegexValidator(
        regex=r'^[6-9]\d{9}$', message="Phone number is not valid")
    phone_number = forms.CharField(validators=[phone_regex], max_length=10, widget=forms.TextInput(
        attrs={'placeholder': 'Enter a valid phone number', 'class': 'mb-4'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter a password', 'class': 'mb-4'}))

    def clean(self, *args, **kwargs):

        phone_number = self.cleaned_data.get('phone_number')
        password = self.cleaned_data.get('password')
        user = authenticate(phone_number=phone_number, password=password)

        if user is None:
            raise forms.ValidationError(
                "Invalid username/password. Please try again!")

        return super(LoginForm, self).clean(*args, **kwargs)

    def login(self, request):
        phone_number = self.cleaned_data.get('phone_number')
        password = self.cleaned_data.get('password')
        user = authenticate(phone_number=phone_number, password=password)

        return user


class RegisterForm(forms.ModelForm):

    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter a confirm password'}))

    class Meta:
        model = User
        fields = ['phone_number', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter a password', 'class': 'mb-4'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter a valid phone number', 'class': 'mb-4'}),
        }
