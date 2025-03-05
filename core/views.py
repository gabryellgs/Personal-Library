from django.shortcuts import render, redirect
from .models import livro
from .forms import LivroForm

# função para listar livros
def telaPrincipal(request):

  # LISTAGEM
  #Variável guardando todos os objetos de livro
  livrinhos = livro.objects.all()

  

  # CADASTRO
  #Variável para guardar fomulário
  formulario = LivroForm(request.POST or None)

  # validação do formulário
  if formulario.is_valid():
    formulario.save()
    return redirect('telaPrincipal')


  # contexto
  contex = {
    # LISTAGEM
    'Livros' : livrinhos,
    # CADASTRO
    'form_livro': formulario,
  }

  # retorno para o html
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



def telaEditar(request, id):

  blivro = livro.objects.get(pk=id)

  formEditar = LivroForm(request.POST or None, instance=blivro) 

  if formEditar.is_valid():
    formEditar.save()
    return redirect('telaPrincipal')
  
  contexto = {
    'form_livro': formEditar
  }

  return render(request, 'telaCadastro.html', contexto )

# função de remover curso
def telaRemover(request, id):
  Removlivro = livro.objects.get(pk=id)
  Removlivro.delete()
  return redirect('telaPrincipal')