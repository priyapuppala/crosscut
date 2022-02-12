from django.shortcuts import render, redirect
from django.http import HttpResponse


def homefunction(request):
    return render(request, "index.html")


def contactfunction(request):
    return render(request, "contact.html")


def aboutfunction(request):
    return render(request, "about.html")


def servicesfunction(request):
    return render(request, "services.html")


def categoryfunction(request):
    return render(request, "category.html")