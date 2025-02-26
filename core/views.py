from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse('olá, Mundo')


def telaP(request):
  return render(request,'telaPrincipal.html')
