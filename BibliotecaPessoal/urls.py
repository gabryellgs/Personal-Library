from django.contrib import admin
from django.urls import path, include
from core.views import telaPrincipal, telaCadastro, telaEditar, telaRemover

urlpatterns = [
    path('telaPrincipal/',telaPrincipal, name='telaPrincipal' ),
    path('telaCadastro/', telaCadastro, name='telaCadastro'),
    path('telaEditar/<int:id>/', telaEditar, name='telaEditar'),
    path('telaRemover/<int:id>/', telaRemover, name='telaRemover'),
    path('api/v1/', include('core.urls_api')),
    path('admin/', admin.site.urls),
]
