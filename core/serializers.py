from rest_framework import serializers
from .models import livro

class Livroserializers(serializers.ModelSerializer):
  class Meta:
    model = livro
    fields = ['id','nome']