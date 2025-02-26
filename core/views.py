from django.shortcuts import render, redirect
from .models import livro


def telaP(request):
  livros = livro.objects.all()
  contex = {
    'Livro' : livros
  }
  return render(request,'telaPrincipal.html', contex)
