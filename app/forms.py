from django import forms 
from .models import Cliente, Endereco, Dependente

# Isso aqui estou lidando com formulário de autenticação do django na tabela AUTH_USER
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = 'rua', 'numero', 'cidade', 'estados'
        widgets = {
            'rua': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),    
            'estados': forms.Select(attrs={'class': 'form-control'}),    
        }


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = 'nome', 'data_nascimento', 'email', 'profissao'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'text'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),    
            'profissao': forms.TextInput(attrs={'class': 'form-control'}),    
        }


class DependenteForm(forms.ModelForm):
    class Meta:
        model = Dependente
        fields = ('nome', 'telefone', 'titular')
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),  
            'titular': forms.Select(attrs={'class': 'form-control'}),    
        }


class UsuarioForm(UserCreationForm):
    # Ela esta cadastrando diretamente no tabela AUTH_USER d
    # o django que ja vem junto dele
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']