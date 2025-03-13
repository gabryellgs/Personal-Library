from django.shortcuts import render, redirect
from .models import livro
from .forms import LivroForm
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Livroserializers




# api
# API DE LISTAR
@api_view(['GET'])
def livroAPIlistar(request):
    livros = livro.objects.all()
    livros_serializers = Livroserializers(livros, many=True)
    return Response(livros_serializers.data)


# API DE CADASTRO
@api_view(['POST'])
def livroAPIadicionar(request):
    livrinhos = Livroserializers(data=request.data)
    if livrinhos.is_valid():
        livrinhos.save()
        return Response(livrinhos.data,status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


# @api_view(['POST'])
# def livroAPIadicionar(request):
#     livros = Livroserializers(data=request.data)
#     if livros.is_valid():
#         livros.save()
#         return Response({'message': 'Nota criada com sucesso!'}, status=status.HTTP_201_CREATED)
#     return Response(livros.errors, status=status.HTTP_400_BAD_REQUEST)



# API PARA EDITAR
@api_view(['PUT'])
def livroAPIeditar(request, id):
    try:
        livro_bd = livro.objects.get(id=id)  # Verifique se o livro com o ID existe
    except livro.DoesNotExist:
        return Response({'message': 'Livro não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    print("Recebido:", request.data)  # 👀 Verificar o que está chegando
    livru = Livroserializers(instance=livro_bd, data=request.data)

    # Atualiza os dados do livro
    livru = Livroserializers(data=request.data, instance=livro_bd)
    if livru.is_valid():
        livru.save()
        return Response(livru.data, status=status.HTTP_202_ACCEPTED)
    else:
        print("Erros do Serializer:", livru.errors)  # 👀 Verificar erro no terminal
        return Response(livru.errors, status=status.HTTP_400_BAD_REQUEST)


# API PARA DELETAR
@api_view(['DELETE'])
def livroAPIremover(request,id):
    livru_bd = livro.objects.get(id=id)
    if(livru_bd):
        livru_bd.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)




# tela principal
def telaPrincipal(request):

  # LISTAGEM
  #Variável guardando todos os objetos de livro
  livrinhos = livro.objects.all()

  

  # CADASTRO
  #Variável para guardar fomulário
  formulario = LivroForm(request.POST or None)

  # Tela de Listagem 
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


#função de editar curso
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