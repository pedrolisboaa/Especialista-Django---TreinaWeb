from django.shortcuts import render
import datetime
from .forms import ClienteForm

# Create your views here.
def index(request):

    horario_atual = datetime.datetime.now()
    form = ClienteForm()

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        print('Dentro do post')
        if form.is_valid():
            print('Formulário cadastrado!')

    

    context = {
        'hora': horario_atual,
        'form': form,
    }
    return render(request, 'index.html', context)