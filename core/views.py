from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from core.models import Slimeline, Event

# Create your views here.
def splash(request):
    if request.user.is_authenticated:
        slimelines = Slimeline.objects.filter(owner=request.user)
        return render(request, "home.html", {"user":request.user, "slimelines":slimelines})
    return render(request, "splash.html", {})


@login_required
def create_slimeline(request):
    if request.method == "POST":
        print("RECEIVED POST REQUEST TO CREATE SLIMELINE")
        print(request.POST.get("name"))
        slimeline = Slimeline.objects.create(name=request.POST.get("name"), owner=request.user)
        return redirect("/")
    if request.method == "GET":
        return render(request, "create_slimeline.html", {})

@login_required
def create_event(request):
    if request.method == "POST":
        event = Event.objects.create(
            author=request.user,
            slimeline=request.POST.get("slimeline"),
            title=request.POST.get("title"),
            content=request.POST.get("content"),
            is_private=request.POST.get("is_private") == "private",
            good_slimes=0,
            start_time=request.POST.get("start_time"),
            end_time=request.POST.get("end_time")
        )
        return redirect("/")
    if request.method == "GET":
        return render(request, "create_event.html", {})

@login_required
def delete_slimeline(request):
    slimeline = Slimeline.objects.get(name=request.GET.get("name"))
    slimeline.delete()
    return redirect("/")

def login_(request):
    if request.method == "POST":
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect("/")
    return render(request, "login.html", {})


def logout_(request):
    logout(request)
    return redirect("/")


def signup_(request):
    if request.method == "POST":
        user = User.objects.create_user(
            email=request.POST['email'],
            username=request.POST['username'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            password=request.POST['password']
        )
        login(request, user)
        print("CREATED USER")
        print(request.POST['email'])
        print(request.POST['password'])
        return redirect('/')
    return render(request, 'signup.html', {})