from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home_page_view, name='home'),
    path('', views.HomePageView.as_view(), name='home'),
]
