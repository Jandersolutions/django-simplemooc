from django.urls import path, include
from .views import index, details

urlpatterns = [
    path('',index, name='index'),
    # busca o id/pk no banco de dados e tras a pagina corespondente com os dados
    path ('<slug:slug>/' , details, name = 'details' ),
]