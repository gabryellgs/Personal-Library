from django.contrib import admin
from django.urls import path
from core.views import telaP

urlpatterns = [
    path('telaP/',telaP ),
    path('admin/', admin.site.urls),
]
