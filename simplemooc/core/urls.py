from django.urls import path, include
from .views import home,contact

urlpatterns = [
    path('',home, name='home'),
    path('contato/',contact,name='contact')
]