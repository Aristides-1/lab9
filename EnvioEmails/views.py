from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):


    send_mail('Hola desde Django y Python',
              'Este es un correo de prueba y automatizado enviado desde Django. SALUDOSSS',
              settings.EMAIL_HOST_USER,
              ['jikin38989@synsky.com'],
              fail_silently=False
              )
    return render(request, 'send/index.html')