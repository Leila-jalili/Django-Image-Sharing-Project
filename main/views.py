from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm

# Create your views here.
def index_view(request):
    return render(request, "index.html")

def view_2(request):
    return HttpResponse("This is view2")
    

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "login.html",
                         {"error": "Invalid username or password", "username": username})

   # print(request.user.is_authenticated)
    #return HttpResponse("Login") 
    return render(request, "login.html", {})

def logout_view(request):
    logout(request)
    return redirect("/")     

def signup_view(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(request, username=form.cleaned_data.get(
                "username"), password=form.cleaned_data.get("password1"))
            if user is not None:
                login(request, user)    
                return redirect("/")
            else:
                return render(request, "signup.html", {"form": form, "error": "Could not login"})

    return render(request, "signup.html", {"form": form})         