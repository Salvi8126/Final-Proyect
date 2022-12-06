from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class libros_venta(models.Model):
    Nombre = models.CharField(max_length=30)
    Autor = models.CharField(max_length=30)
    Salida = models.DateField( null=True)
    email = models.EmailField(max_length=30, null=True)
    def __str__(self):
        return " %s %s" % (self.Nombre, self.Autor)

#class Avatar(models.Model):

    #user= models.ForeignKey(User, on_delete=models.CASCADE)

    #imagen= models.ImageField(upload_to="avatares", null= True, blank=True)

    #def __str__(self):
        #return  f"{self.user}-{self.imagen}"


