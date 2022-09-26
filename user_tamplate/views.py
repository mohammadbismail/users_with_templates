from pyexpat import model
from django.shortcuts import render, redirect
from .models import User
from user_tamplate import models


def index(request):
    context = {
        "users": models.getAll(),
    }
    return render(request, "index.html", context)


def process(request):
    # if models.isAuthenticated(request):
    models.createUser(request)
    return redirect("/")
    # else:
    # return redirect("/Login")
