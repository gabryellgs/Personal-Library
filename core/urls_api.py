from django.urls import path
from .views import livroAPIlistar, livroAPIadicionar, livroAPIeditar, livroAPIremover


urlpatterns = [
  path('livros/listar/', livroAPIlistar, name="listar"),
  path('livros/adicionar/', livroAPIadicionar, name="adicionar"),
  path('livros/editar/<int:id>/', livroAPIeditar, name="editar"),
  path('livros/remover/<int:id>/', livroAPIremover, name="remover"),
]