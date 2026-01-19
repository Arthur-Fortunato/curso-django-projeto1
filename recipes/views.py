from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'recipes/home.html', context= {
        'name': 'Arthur Ribeiro'
    })

def contato(request):
    return HttpResponse("CONTATO") 

def sobre(request):
    return render(request, 'me-apague/temp.html')