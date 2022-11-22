from django.contrib import admin
from Blog.models import libros_venta


class LibrosAdmin(admin.ModelAdmin):
    list_display = ("Nombre", "Autor", "Salida", "email")

#class PadreAdmin(admin.ModelAdmin):
    #list_display = ("Nombre", "Apellido", "Birthday", "profesion", "email")

#class HermanoAdmin(admin.ModelAdmin):
    #list_display = ("Nombre", "Apellido", "Birthday", "profesion", "email")

admin.site.register(libros_venta, LibrosAdmin)
#admin.site.register(Padre, PadreAdmin)
#admin.site.register(Hermano, HermanoAdmin)
