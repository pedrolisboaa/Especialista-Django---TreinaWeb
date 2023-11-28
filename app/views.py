from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Cliente
from .forms import ClienteForm
# Create your views here.
def index(request):
    
    
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClienteForm()
            
    context = {
        'form': form,
    }
        
    return render(request, 'index.html', context)


def listar(request):
    clientes = Cliente.objects.order_by('id')
    context = {
        'clientes': clientes,
    }
    
    return render(request, 'listar.html', context)


def atualizar(request, id_cliente):
    cliente = Cliente.objects.get(pk=id_cliente)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
    else:
        form = ClienteForm(instance=cliente)
            
    context = {
        'cliente': cliente,
        'form': form,
    }
    return render(request, 'atualizar.html', context)


def deletar(request, id_cliente):
    cliente = Cliente.objects.get(pk=id_cliente)
    if request.method == 'POST':
        cliente.delete()
        return redirect('index')

    return render(request, 'deletar.html', {'cliente': cliente})
    
