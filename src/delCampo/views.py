from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request, "home.html", {"title": "Home"})

def login_page(request):
    return render(request, "login.html", {"title": "Login"})
