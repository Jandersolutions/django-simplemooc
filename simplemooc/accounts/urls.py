from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView,LogoutView
from . import views

urlpatterns = [
    path('entrar/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('sair/', LogoutView.as_view(next_page='/'), name='logout'),
]