from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from account.forms import LoginUserForm ,RegisterUserForm
from django.contrib import messages
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt


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
                return redirect('block/index')
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
    return redirect('index')