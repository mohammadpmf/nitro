from django.shortcuts import render

from . import models


def show_info(request):
    teachers = models.Teacher.objects.all()
    context = { 'teachers': teachers}
    return render(request, 'teachers/index.html', context)