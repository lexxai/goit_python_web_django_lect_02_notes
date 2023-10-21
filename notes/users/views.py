from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm, RegisterForm, LoginForm, DeleteForm


def signupuser(request):
    if request.user.is_authenticated:
        return redirect(to="noteapp:main")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="users:login")
        else:
            return render(request, "users/signup.html", context={"form": form})

    return render(request, "users/signup.html", context={"form": RegisterForm()})




def loginuser(request):
    if request.user.is_authenticated:
        return redirect(to="noteapp:main")

    if request.method == "POST":
        user = authenticate(
            username=request.POST["username"], password=request.POST["password"]
        )
        if user is None:
            messages.error(request, "Username or password didn't match")
            return redirect(to="users:login")

        login(request, user)
        return redirect(to="noteapp:main")

    return render(request, "users/login.html", context={"form": LoginForm()})


@login_required
def logoutuser(request):
    logout(request)
    return redirect(to='noteapp:main')


# @login_required
# def profile(request):
#     return render(request, 'users/profile.html')



@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users:profile')

    profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'users/profile.html', {'profile_form': profile_form})


@login_required
def deleteuser(request):
    if not request.user.is_authenticated:
        return redirect(to="noteapp:main")

    if request.method == "POST":
        form = DeleteForm(request.POST)
        if form.data.get("username") == request.user.username:       
            if request.user.delete():
                messages.success(request, 'User was deleted successfully')
                return redirect(to="noteapp:main")
            else:
                messages.error(request, 'User was not deleted')
        else:
            messages.error(request, f'User was not deleted. Data of form is wrong {form.data["username"]=}, {request.user.username=}')

    return render(request, "users/delete.html", context={"form": DeleteForm(), "username":request.user })



# Create your views here.
