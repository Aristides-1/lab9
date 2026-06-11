from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):


    send_mail('Hola desde Django y Python',
              'Este es un correo de prueba y automatizado enviado desde Django. SALUDOSSS',
              'diegozc792@gmail.com',
              ['yetises553@fixscal.com'],
              fail_silently=False
              )
    return render(request, 'index.html')