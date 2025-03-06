from django.urls import path
from .views import livroAPIlistar, livroAPIadicionar
# ,areaAPIatualizar,areaAPIremover


urlpatterns = [
  path('livros/listar/', livroAPIlistar, name="listar"),
  path('livros/adicionar/', livroAPIadicionar, name="adicionar"),
  # path('areas/atualizar/<int:id>/', areaAPIatualizar, name="atualizar"),
  # path('areas/remover/<int:id>/', areaAPIremover, name="remover"),
]