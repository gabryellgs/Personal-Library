from django.contrib import admin
from django.urls import path
from core.views import telaPrincipal, telaCadastro, telaEditar

urlpatterns = [
    path('telaPrincipal/',telaPrincipal, name='telaPrincipal' ),
    path('telaCadastro/', telaCadastro, name='telaCadastro'),
    path('telaEditar/<int:id>/', telaEditar, name='telaEditar'),
    path('admin/', admin.site.urls),
]
