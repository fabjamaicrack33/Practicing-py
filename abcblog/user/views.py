from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(request):
    return HttpResponse('hello, you are at the login')

def register(request):
    return HttpResponse('Hello you are at the register')