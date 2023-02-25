from django.shortcuts import render
from django.views import generic

def home_page_view(request):
    return render(request, "home.html")

class HomePageView(generic.TemplateView): # TemplateView یه ویو خالی هست که میتونیم اسم تمپلیت رو بهش بدیم.
    template_name = "home.html"
