from django.contrib import admin
from django.urls import path
from core.views import telaPrincipal

urlpatterns = [
    path('telaPrincipal/',telaPrincipal, name='telaPrincipal' ),
    path('admin/', admin.site.urls),
]
