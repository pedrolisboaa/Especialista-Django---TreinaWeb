from django.urls import path
from .views import index, atualizar, deletar, cadastro

urlpatterns = [
   path('', index, name='index'),
   path('cadastro/', cadastro, name='cadastro'),
   path('atualizar/<int:id_cliente>', atualizar, name='atualizar'),
   path('deletar/<int:id_cliente>', deletar, name='deletar'),
]
