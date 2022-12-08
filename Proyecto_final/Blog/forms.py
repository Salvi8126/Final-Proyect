#from Blog.models import Avatar

#class AvatarForm(forms.ModelForm):
    #class Meta:
        #model = Avatar
        #fields = ("image", )

from django import forms

from Blog.models import libros_venta

class libros_ventaForm(forms.ModelForm):
    Nombre = forms.CharField(
        label="Nombre del comprador",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "buyers-name",
                "placeholder": "Nombre del comprador",
                "required": "True",
            }
        ),
    )
    Autor = forms.CharField(
        label="Normbre del autor",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "autor-name",
                "placeholder": "Nombre del autor",
                "required": "True",
            }
        ),
    )
    Salida = forms.DateField(
        label="Fecha de lanzamiento",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "book-release-date",
                "placeholder": "Fecha de lanzamiento",
                "required": "True",
            }
        ),
    )
    Email = forms.EmailField(
        label="Correo electronico del comprador",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "buyers-email",
                "placeholder": "email",
                "required": "True",
            }
        ),
    )
    class Meta:
        model = libros_venta
        fields = ["Nombre", "Autor", "Salida", "Email"]