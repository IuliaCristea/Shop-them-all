from django.http import HttpRequest
from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def realogin(request):
    return render(request, 'realogin.html')

def home(request):
    return HttpRequest("prima pagina")
