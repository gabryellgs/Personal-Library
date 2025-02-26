from django.forms import ModelForm
from .models import livro


class livroForm (ModelForm):
  class Meta:
    model = livro
    fields = ['titulo', 'status']