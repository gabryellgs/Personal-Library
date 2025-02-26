from django.db import models

class livro(models.Model):
  titulo = models.CharField('Título', max_length=50)
  status = models.CharField('Status', max_length=10)