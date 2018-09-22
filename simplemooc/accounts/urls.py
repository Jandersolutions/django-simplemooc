from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . views import register,dashboard,edit,edit_password,password_reset,password_reset_confirm

urlpatterns = [
    path('',dashboard,name='dashboard'),
    path('entrar/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('sair/', LogoutView.as_view(next_page='/'), name='logout'),
    path('cadastrar/',register,name='register'),
    path('editar/',edit,name='edit'),
    path('nova_senha/',password_reset,name='password_reset'),
    path('confirmar_nova_senha/(?P<key>\w+)/$',password_reset_confirm,name='password_reset_confirm'),
    path('editar_senha/',edit_password,name='edit_password'),
]