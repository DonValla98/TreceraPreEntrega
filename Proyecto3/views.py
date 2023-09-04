from django.shortcuts import render
from django.http import HttpResponse
from AppProyecto.models import Curso

def curso(request):

    curso = Curso(nombre="Python", descripcion="Curso de Python para principiantes")
    curso.save()
    documento_de_texto = f"Curso: {curso.nombre}, Descripción: {curso.descripcion}"
    
    return HttpResponse(documento_de_texto)
