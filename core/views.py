from django.shortcuts import render, redirect
from .models import livro
from .forms import livroForm

def telaP(request):
  livros = livro.objects.all()
  contex = {
    'Livro' : livros
  }
  return render(request,'telaPrincipal.html', contex)

def livro_cadastrar(request):
  form = livroForm(request.POST or None)

  if form.is_valid():
    form.save()
    return redirect('telaP')

  contex = {
    'form_livro': form
  }
  return render(request, 'livro_cadastrar.html', contex)