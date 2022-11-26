from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=40)
    birth_date = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    adress = models.CharField(max_length=40)
    list_display = ("name", "birth_date", "last_name", "adress")
    
    def __str__(self):
        return f"{self.name} {self.last_name} | information : {self.birth_date} {self.adress}"