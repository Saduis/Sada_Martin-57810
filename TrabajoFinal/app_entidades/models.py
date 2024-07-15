from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Libro (models.Model):
    nombre = models.CharField( max_length=200 )
    autor =  models.CharField( max_length=50)
    anio_edicion = models.IntegerField()
    editorial = models.CharField( max_length=50)

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ["nombre","autor"]

    def __str__(self):
        return f"{self.nombre}, {self.autor}"

class Autor (models.Model):
    nombre = models.CharField( max_length=50)
    apellido = models.CharField( max_length=50)
    nacionalidad = models.CharField( max_length=50)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ["apellido","nombre"]
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Prestamo (models.Model):
    nombre = models.CharField( max_length=50)
    apellido = models.CharField( max_length=50)
    libro = models.CharField(max_length=100, null=True)
    fecha_prestamo = models.DateField(null=False)
    fecha_devolucion = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Préstamo"
        verbose_name_plural = "Préstamos"
        ordering = ["apellido","nombre"]

    def __str__(self):
        return f"{self.apellido}, {self.nombre}, {self.fecha_prestamo}"
    
class Lector (models.Model):
    nombre = models.CharField( max_length=50)
    apellido = models.CharField( max_length=50)
    email = models.EmailField()

    class Meta:
        verbose_name = "Lector/Lectora"
        verbose_name_plural = "Lectores"
        ordering = ["apellido","nombre"]
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user} {self.imagen}"
