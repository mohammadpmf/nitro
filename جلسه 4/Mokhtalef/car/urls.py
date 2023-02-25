from django.urls import path
from . import views

urlpatterns = [
    path('pride/', views.show_pride, name='pride'),
    path('lamborghini/', views.show_lamborghini, name='lambor'),
    path('', views.show_home, name='home'),
]
