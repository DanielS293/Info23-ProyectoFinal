from django.shortcuts import render

def inicio(request):
    return render(request, 'blog/inicio.html')

def categoria(request):
    return render(request, 'blog/categoria.html')