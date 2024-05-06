from django import forms
from django.contrib.auth.forms  import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import widgets


class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget = widgets.TextInput(attrs={
                "class":"form-control",
                "placeholder" : "Enter your username here"
            })

        self.fields["password"].widget = widgets.PasswordInput(attrs={
                "class":"form-control",
                "placeholder" : "Password"
            })


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already used")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This email username is already used.")
        return username