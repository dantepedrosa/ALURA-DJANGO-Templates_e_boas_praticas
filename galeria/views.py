from django.shortcuts import render

def index(request):
    return render(request, 'galeria/index.html')

def imagem(request):
    # TODO - Criar imagem 
    return render(request, 'galeria/imagem.html')