from django.http import HttpResponse
from datetime import datetime
import json

def hola(request):
    dia=datetime.now().day
    mes=datetime.now().month
    year=datetime.now().year
    fecha=str(dia)+'/'+str(mes)+'/'+str(year)
    hora=datetime.now().hour
    minutos=datetime.now().minute
    hour=str(hora)+':'+str(minutos)
    numeros=sorted([int(i) for i in str(request.GET["numbers"]).split(',')])
    cad=f'Hola <strong>José</strong> hoy es {fecha} y son las {hour} <br>numeros {numeros}'
    data={
        'status': 'ok',
        'numbers': numeros,
        'message': 'Integers sorted succesfully'
    }
    return HttpResponse(json.dumps(data,indent=4),content_type='application/json')


def say_hi(request, name, age):
    if age<18:
        message='Sorry {}, you are a child'.format(name)
    else:
        message='Hello {}, welcome to the future'.format(name)
    return HttpResponse(message)