from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from .models import *
from .forms import *


# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def signup(request):
    if request.method == "POST":
        form1 = UserSignupForm(request.POST)
        form2 = ProfileSignupForm(request.POST)
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1!=password2:
            messages.warning(request, "Password and Confirm Password is not Same")
            return redirect("signup")
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.set_password(password1)
            user.save()
            profile = form2.save(commit = False)
            profile.user = user
            profile.save()
            messages.success(request, "Successfully Registered")
            return redirect("signup")
        else:
            messages.warning(request, "Not Valid Data")
            return redirect("signup")
    context = {
        "form1": UserSignupForm(),
        "form2": ProfileSignupForm(),
    }
    return render(request,"home/signlog.html",context)


def login(request):
    if request.method == "POST":
        user = auth.authenticate(
            request,
            username=request.POST["email"],
            password=request.POST["password"]
        )
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Wrong Credentials! Please try again")
            return redirect("login")
    return render(request, "home/signlog.html")


def logout(request):
    if request.user:
        auth.logout(request)
    return redirect('login')
