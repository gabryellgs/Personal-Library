from django.shortcuts import render, redirect
from .models import livro


def telaPrincipal(request):
  livrinhos = livro.objects.all()
  contex = {
    'Livros' : livrinhos
  }

  return render(request,'telaPrincipal.html', contex)
