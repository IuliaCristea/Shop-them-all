from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def home(request):
    return HttpResponse("First Page")
