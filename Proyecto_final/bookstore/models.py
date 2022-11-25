from django.db import models

# Create your models here

class BookStore(models.Model):
    name = models.CharField(max_length=40)
    owner = models.CharField(max_length=40)
    adress = models.CharField(max_length=40)
    list_display = ("name", "owner", "adress")
    
    def __str__(self):
        return f"{self.name} {self.adress} | owner: {self.owner}"