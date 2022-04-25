from django.http import HttpResponse
import datetime

def saludo(request):

    documento = """
        <html>
        <body><h1>Hola</h1></body></html>
    """
    return HttpResponse(documento)

def despedida(request):

    return HttpResponse("Adios")

def dameFecha(request):

    fecha_actual=datetime.datetime.now()
    documento = """
        <html><body><h1>
        Fecha y hora actual: %s 
        </h1></body></html>
    """ % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request,actual, edad):

    periodo= edad-2022
    edadFutura= actual + periodo
    documento = """
        <html>
        <body><h1>En el año %s tendras %s</h1></body></html>
    """ %(edad, edadFutura)

    return HttpResponse(documento)