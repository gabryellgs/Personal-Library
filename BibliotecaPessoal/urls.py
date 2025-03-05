from django.contrib import admin
from django.urls import path
from core.views import telaPrincipal, telaCadastro

urlpatterns = [
    path('telaPrincipal/',telaPrincipal, name='telaPrincipal' ),
    path('telaCadastro/', telaCadastro, name='telaCadastro'),
    path('admin/', admin.site.urls),
]
