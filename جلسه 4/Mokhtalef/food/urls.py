from django.urls import path
from . import views

urlpatterns = [
    path('pizza/', views.show_pizza, name='pizza'),
    path('french fries/', views.show_french, name='french_fries'),
    path('spaghetti/', views.show_spaghetti, name='spaghetti'),
]
