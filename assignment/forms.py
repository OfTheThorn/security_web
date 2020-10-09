from django_registration import forms
from django_registration.forms import RegistrationForm
from django.contrib.auth.models import User

class RegisterForm(RegistrationForm):
    username = RegistrationForm.username
    password1 = RegistrationForm.password1
    password2 = RegistrationForm.password2
    email = forms.RegistrationFormUniqueEmail

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
