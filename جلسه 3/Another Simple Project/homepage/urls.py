from django.urls import path, include
from . import views

urlpatterns = [
    path('b/', views.say_hello, name="say_hello"),
    path('home page/', views.my_home_page, name="home_page"),
]
