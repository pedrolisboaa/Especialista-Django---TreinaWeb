from django.shortcuts import render, redirect
import datetime
from django.views.generic import CreateView
from .models import Cliente

# Create your views here.
class ClienteCreateView(CreateView):
    mode = Cliente
    fields = '__all__'
    template_name = 'index.html'