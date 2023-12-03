from django.urls import path
from .views import index, atualizar, deletar, cadastro, dependente
from .views import usuarioCadastrar

urlpatterns = [
   path('', index, name='index'),
   # Cliente
   path('cadastro/', cadastro, name='cadastro'),
   path('atualizar/<int:id_cliente>', atualizar, name='atualizar'),
   path('deletar/<int:id_cliente>', deletar, name='deletar'),
   # Dependente
   path('dependente/', dependente, name='dependente'),
   # Usuario
   path('usuario_cadastrar/', usuarioCadastrar, name='usuario_cadastrar'),
]
