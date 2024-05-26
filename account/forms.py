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
        fields = ("first_name","last_name","username","email",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget = widgets.TextInput(attrs={"class":"form-control"})
        self.fields["last_name"].widget = widgets.TextInput(attrs={"class":"form-control"})
        self.fields["username"].widget = widgets.TimeInput(attrs={"class":"form-control"})
        self.fields["email"].widget = widgets.EmailInput(attrs={"class":"form-control"})
        self.fields["email"].required = True
        self.fields["password1"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["password2"].widget = widgets.PasswordInput(attrs={"class":"form-control"})

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error("email","This address already used")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            self.add_error("username","This username already used")
        return username
    

class PasswordChangeForm(forms.Form):
    old_password = forms.CharField(label='Eski Şifre', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='Yeni Şifre', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Yeni Şifre Tekrar', widget=forms.PasswordInput)

