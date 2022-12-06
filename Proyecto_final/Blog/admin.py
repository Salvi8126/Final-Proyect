from django.contrib import admin
from Blog.models import libros_venta
from bookstore.models import BookStore
from employees.models import Employee




class LibrosAdmin(admin.ModelAdmin):
    list_display = ("Nombre", "Autor", "Salida", "email")

class BookstoreAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "adress")

admin.site.register(libros_venta, LibrosAdmin )

admin.site.register(BookStore, BookstoreAdmin)

admin.site.register(Employee)

