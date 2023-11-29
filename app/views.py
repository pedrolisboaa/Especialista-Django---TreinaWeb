from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Cliente, Endereco
from .forms import ClienteForm, EnderecoForm
# Create your views here.

def index(request):
    clientes = Cliente.objects.order_by('id')
    context = {
        'clientes': clientes,
    }
    
    return render(request, 'index.html', context)


def cadastro(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST, prefix='cliente')
        endereco_form = EnderecoForm(request.POST, prefix='endereco')
        
        if cliente_form.is_valid() and endereco_form.is_valid():
            cliente = cliente_form.save(commit=False)
            endereco = endereco_form.save()
            cliente.endereco = endereco
            cliente.save()
            return redirect('index')
    else:
        cliente_form = ClienteForm(prefix='cliente')
        endereco_form = EnderecoForm(prefix='endereco')
        
    context = {
        'cliente_form': cliente_form,
        'endereco_form': endereco_form,
    }

        
    return render(request, 'cadastro.html', context)


def atualizar(request, id_cliente):
    cliente = Cliente.objects.get(pk=id_cliente)
    endereco = cliente.endereco
    
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST, instance=cliente, prefix='cliente')
        endereco_form = EnderecoForm(request.POST, instance=endereco, prefix='endereco')
        
        if cliente_form.is_valid() and endereco_form.is_valid():
            cliente = cliente_form.save(commit=False)
            endereco = endereco_form.save()
            cliente.endereco = endereco
            cliente.save()
            return redirect('index')
    else:
        cliente_form = ClienteForm(instance=cliente, prefix='cliente')
        endereco_form = EnderecoForm(instance=endereco, prefix='endereco')
            
    context = {
        'cliente': cliente,
        'cliente_form': cliente_form,
        'endereco_form': endereco_form
    }
    return render(request, 'atualizar.html', context)

def deletar(request, id_cliente):
    cliente = Cliente.objects.get(pk=id_cliente)
    endereco = cliente.endereco
    
    if request.method == 'POST':
        endereco.delete()
        cliente.delete()
        return redirect('index')

    return render(request, 'deletar.html', {'cliente': cliente})


