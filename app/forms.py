from django import forms 
from .models import Cliente, Endereco


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


