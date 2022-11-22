from ast import Return
from django.shortcuts import render
from django.http import HttpResponse
from Blog.models import libros_venta

# Create your views here.

def home(request):

    return render(request, "BlogApp/home.html")

def Libros(request):

    Libro= libros_venta.objects.all()
    
    return render(request, "BlogApp/post.html", {"Venta de libros": libros_venta})
    
