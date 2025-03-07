from django.urls import path
from .views import livroAPIlistar, livroAPIadicionar, livroAPIatualizar, livroAPIremover
# ,areaAPIatualizar,areaAPIremover


urlpatterns = [
  path('livros/listar/', livroAPIlistar, name="listar"),
  path('livros/adicionar/', livroAPIadicionar, name="adicionar"),
  path('livros/atualizar/<int:id>/', livroAPIatualizar, name="atualizar"),
  path('livros/remover/<int:id>/', livroAPIremover, name="remover"),
]