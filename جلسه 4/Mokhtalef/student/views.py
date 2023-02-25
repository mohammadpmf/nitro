from django.shortcuts import render
from django.http import HttpResponse


def arad(request):
    return HttpResponse("I am Arad")


def behrad(request):
    return HttpResponse("I am Behrad")
