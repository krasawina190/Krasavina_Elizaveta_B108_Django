from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Добро пожаловать на Адвито!')

def categories(request):
    return HttpResponse('Категории:')