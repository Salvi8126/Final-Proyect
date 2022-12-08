from ast import Return
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from Blog.models import libros_venta
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from Blog.forms import libros_ventaForm
from django.core.exceptions import ValidationError
#from Blog.forms import AvatarForm





@login_required
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
             
           return redirect("/")
        else:
            for msg in form.error_messages:
                
              messages.error(request, form.error_messages[msg])

            return render(request, "BlogApp/registration/login.html", {"form":form})

        
       

def index(request):
   


    return render(request, "BlogApp/home.html")


def salir(request):
    logout(request)
    return redirect("/")

def Libros(request):

    Libro= libros_venta.objects.all()
    
    return render(request, "BlogApp/post.html", {"Venta de libros": libros_venta})

def about(request):
   


    return render(request, "BlogApp/about.html")

def bookstore(request):

    return render(request, "BlogApp/bookstore.html")


class libros_ventaListView(ListView):
    model = libros_venta
    paginate_by = 3
    template_name = "libros_venta_list.html"


class libros_ventaDetailView(DetailView):
    model = libros_venta
    fields = ["Nombre", "Autor", "Salida", "Email"]
    template_name = "libros_venta_detail.html"


class libros_ventaCreateView(LoginRequiredMixin, CreateView):
    model = libros_venta
    success_url = reverse_lazy("libros_venta:libros_venta-list")

    form_class = libros_ventaForm

    def form_valid(self, form):
        data = form.cleaned_data
        actual_objects = libros_venta.objects.filter(
            Nombre=data["Nombre"],
            Autor=data["Autor"],
            Salida=data["Salida"],
            Email=data["Email"],
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El comprador {data['Nombre']} | {data['Email']} ya está creada",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Comprador: {data['Nombre']} - {data['Email']}. Creado exitosamente!",
            )
            return super().form_valid(form)


class libros_ventaUpdateView(LoginRequiredMixin, UpdateView):
    model = libros_venta
    fields = ["Nombre", "Autor", "Salida", "Email"]

    def get_success_url(self):
        libros_venta_id = self.kwargs["pk"]
        return reverse_lazy("libros_venta:libros_venta-detail", kwargs={"pk": libros_venta_id})


class libros_ventaDeleteView(LoginRequiredMixin, DeleteView):
    model = libros_venta
    success_url = reverse_lazy("libros_venta:libros_venta-list")
