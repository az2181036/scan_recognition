from django.shortcuts import render

def index(request):
    return render(request, 'index.html',)

def database(request):
    return render(request, 'database.html',)