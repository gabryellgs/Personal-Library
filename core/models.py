from django.db import models

STATUS_CHOICES = (
  ('Lendo', 'Lendo'),
  ('Finalizado', 'Finalizado'),
  ('Deseja-se', 'Deseja-se')
)
class livro(models.Model):
  titulo = models.CharField('Título', max_length=50)
  status = models.CharField('Status', max_length=12, choices=STATUS_CHOICES)