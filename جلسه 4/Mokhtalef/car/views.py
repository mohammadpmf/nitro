from django.shortcuts import render
from django.http import HttpResponse


def show_home(request):
    return HttpResponse("Welcome to My car shop")


def show_pride(request):
    return HttpResponse("Hello pride")


def show_lamborghini(request):
    return HttpResponse("Hello lamborghini")
