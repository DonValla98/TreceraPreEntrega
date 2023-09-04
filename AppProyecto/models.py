from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    
class Entregable(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_entrega = models.DateField()
    curso_relacionado = models.ForeignKey(Curso, on_delete=models.CASCADE)