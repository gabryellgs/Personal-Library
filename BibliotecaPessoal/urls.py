from django.contrib import admin
from django.urls import path
from core.views import index, telaP

urlpatterns = [
    path('index/',index),
    path('telaP/',telaP ),
    path('admin/', admin.site.urls),
]
