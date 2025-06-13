from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('user', views.get_user, name='get_user'),
    path('change-password', views.change_password, name='change_password'),
]