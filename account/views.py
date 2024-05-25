from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from account.forms import ChangePasswordForm, LoginUserForm ,RegisterUserForm
from django.contrib import messages
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import update_session_auth_hash






@csrf_exempt
def user_login(request):
    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None and user.is_active:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'account/login.html', {'form': form})
        else:
            return render(request, 'account/login.html', {'form': form})

    form = LoginUserForm()
    return render(request, 'account/login.html', {'form': form})
               

@csrf_exempt
def user_register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_login")
        else:
            return render(request, "account/register.html",{"form":form})
    
    form = RegisterUserForm()
    return render(request, "account/register.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect('homepage')


def password_change(request):
    if request.method == 'POST':
        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = request.user
            old_password = form.cleaned_data['old_password']
            new_password1 = form.cleaned_data['new_password1']
            new_password2 = form.cleaned_data['new_password2']
            if user.check_password(old_password):
                if new_password1 == new_password2:
                    user.set_password(new_password1)
                    user.save()
                    update_session_auth_hash(request, user)
                    
                    return render(request, 'succes.html', {'form': form})
                else:
                    messages.error(request, 'Yeni şifreler uyuşmuyor.')
            else:
                messages.error(request, 'Eski şifreniz doğru değil.')
                
    else:
        form = ChangePasswordForm()
        
        form.helper = None

    # Crispy Forms kullanarak form alanlarını biçimlendir
    form.fields['old_password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Eski Şifreniz'})
    form.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Yeni Şifreniz'})
    form.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Yeni Şifrenizi Tekrar Girin'})

    return render(request, 'password_change.html', {'form': form})