from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render (request, 'generador/home.html')


def about(request):
    return render (request, 'generador/about.html')
    
def password(request):

    caracteres = list('abcdefghijklmnopqrstuvwxyz')
    password_generada = ''

    longitud = int(request.GET.get('longitud'))
    
    if request.GET.get('mayuscula'):
        caracteres.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('especial'):
        caracteres.extend(list('!@#$%&/()=¿¡<>+*-_[{]}¨'))

    if request.GET.get('numeros'):
        caracteres.extend(list('0123456789'))    
    
    for x in range(longitud):
        password_generada += random.choice(caracteres) 

    return render (request, 'generador/password.html', {'password':password_generada })

