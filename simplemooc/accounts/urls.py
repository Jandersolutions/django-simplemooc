from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView,LogoutView
from . import views
from . views import register,dashboard,edit,edit_password

urlpatterns = [
    path('',dashboard,name='dashboard'),
    path('entrar/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('sair/', LogoutView.as_view(next_page='/'), name='logout'),
    path('cadastrar/',register,name='register'),
    path('editar/',edit,name='edit'),
    path('editar_senha/',edit_password,name='edit_password'),
]