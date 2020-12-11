from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['phone_number', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter a password', 'class': 'mb-4'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter a valid phone number', 'class': 'mb-4'}),
        }

    def clean(self):
        super(LoginForm,self).clean()
        print("Clean")

        phone_number = self.cleaned_data.get('phone_number')
        password = self.cleaned_data.get('password')
        print(phone_number)

        return self.cleaned_data
