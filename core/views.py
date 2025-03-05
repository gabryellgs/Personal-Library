from django.shortcuts import render, redirect
from .models import livro
from .forms import LivroForm


def telaPrincipal(request):
  livrinhos = livro.objects.all()
  contex = {
    'Livros' : livrinhos
  }

  return render(request,'telaPrincipal.html', contex)


def telaCadastro(request):
  formulario = LivroForm(request.POST or None)

  if formulario.is_valid():
    formulario.save()
    return redirect('telaPrincipal')

  contexto = {
    'form_livro': formulario
  }
  return render(request,'telaCadastro.html', contexto)