from django.contrib import admin
from .models import Cliente, Endereco, Dependente, Atendente

# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = 'nome', 'data_nascimento', 'email', 'profissao', 'endereco'
    autocomplete_fields = ['endereco']
    
@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = 'rua',
    search_fields = ['rua']


@admin.register(Dependente)
class DependenteAdmin(admin.ModelAdmin):
    list_display = 'nome', 'telefone', 'titular'
    search_fields = 'dependente',


