from django.urls import path
from . import views

urlpatterns = [
    path('arad/', views.arad, name='arad'),
    path('behrad/', views.behrad, name='behrad'),
]
