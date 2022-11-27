from ast import Return
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Blog.models import libros_venta
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

@login_required


def salir(request):
    logout(request)
    return redirect("/")

def home(request):

    return render(request, "BlogApp/home.html")

def Libros(request):

    Libro= libros_venta.objects.all()
    
    return render(request, "BlogApp/post.html", {"Venta de libros": libros_venta})
    
