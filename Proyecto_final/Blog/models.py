from django.db import models

# Create your models here.
class libros_venta(models.Model):
    Nombre = models.CharField(max_length=30)
    Autor = models.CharField(max_length=30)
    Salida = models.DateField( null=True)
    email = models.EmailField(max_length=30, null=True)
    def __str__(self):
        return " %s %s" % (self.Nombre, self.Autor)


