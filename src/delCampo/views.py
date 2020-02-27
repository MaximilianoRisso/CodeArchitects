from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def home_page(request):
    return render(request, "home.html", {"title": "Home"})


