from django import forms 

class ClienteForm(forms.Form):
    nome = forms.CharField(label='Nome Cliente', max_length=100)
    idade = forms.IntegerField(label='Idade')
    is_ativo = forms.BooleanField(label='Se o cliente esta')