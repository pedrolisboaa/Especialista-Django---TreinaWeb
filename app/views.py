from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Cliente, Endereco, Dependente
from .forms import ClienteForm, EnderecoForm, DependenteForm, UsuarioForm
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    clientes = Cliente.objects.order_by('id')
    usuarios = User.objects.order_by('id')
    context = {
        'clientes': clientes,
        'usuarios': usuarios
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


def dependente(request):
    
    dependentes = Dependente.objects.order_by('id')
    
    form = DependenteForm()
    context = {
        'form': form,
    }
    
    if request.method == 'POST':
        form = DependenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dependente')
    else:
          form = DependenteForm()
          
    context = {
        'form': form,
        'dependentes': dependentes,
    }
        

    return render(request, 'dependente.html', context)


# Usuário

def usuarioCadastrar(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            print('VOU SALVAR')
            return redirect('index')
    else:
        form = UsuarioForm()
        print('DEU RUIM')

    context = {
        'form': form,
    }
    return render(request, 'usuario_cadastrar.html', context)