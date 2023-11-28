from django.urls import path
from .views import index, atualizar, deletar, listar

urlpatterns = [
   path('', index, name='index'),
   path('listar/', listar, name='listar'),
   path('atualizar/<int:id_cliente>', atualizar, name='atualizar'),
   path('deletar/<int:id_cliente>', deletar, name='deletar'),
   
]
