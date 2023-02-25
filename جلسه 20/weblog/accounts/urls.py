from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.sign_up_view, name='signup'),
    # path('signup/', views.SignUpView.as_view(), name='signup'), # این مدل کلس بیسد هست.
]
