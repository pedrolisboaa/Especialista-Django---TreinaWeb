from django import forms 
from .models import Cliente

# class ClienteForm(forms.Form):
#     nome = forms.CharField(label='Nome Cliente', max_length=100)
#     idade = forms.IntegerField(label='Idade')
#     is_ativo = forms.BooleanField(label='Se o cliente esta')


# Gerando formulário conforme MODEL do banco de dados

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = 'nome', 'data_nascimento', 'email', 'profissao',
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),    
            'profissao': forms.TextInput(attrs={'class': 'form-control'}),    
        }
