from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.show_homepage, name='homepage'),
    path('amir/', views.show_amir, name='amir'),
    path('ali/', views.show_ali, name='ali'),
    path('abbas/', views.show_abbas, name='abbas'),
]
