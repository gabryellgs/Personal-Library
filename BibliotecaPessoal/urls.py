from django.contrib import admin
from django.urls import path
from core.views import telaP, livro_cadastrar

urlpatterns = [
    path('telaP/',telaP, name='telaP' ),
    path('livro_cadastrar/', livro_cadastrar, name='livro_cadastrar'),
    path('admin/', admin.site.urls),
]
