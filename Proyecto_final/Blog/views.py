from ast import Return
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from Blog.models import libros_venta
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View

#@login_required
# Create your views here.
class VRegistro(View):
    def get(self, request):
        form=UserCreationForm
        return render(request, "BlogApp/registration/login.html", {"form":form})
    
    def post(self, request):
        form=UserCreationForm(request.POST)

        if form.is_valid():
            
            usuario=form.save()
            
            login(request, usuario)
            
            return redirect("home")
        
        else:
            pass


#def login(request):

    #return render(request, "BlogApp/registration/login.html")
def home(request):


    return render(request, "BlogApp/home.html")


def salir(request):
    logout(request)
    return redirect("/")

def Libros(request):

    Libro= libros_venta.objects.all()
    
    return render(request, "BlogApp/post.html", {"Venta de libros": libros_venta})
    
