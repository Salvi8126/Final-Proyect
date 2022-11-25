from django import forms

from bookstore.models import BookStore

class BookStoreForm(forms.ModelForm):
    name = forms.CharField(
        label="Nombre de la Libreria",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "bookstore-name",
                "placeholder": "Nombre de la Libreria",
                "required": "True",
            }
        ),
    )
    last_name = forms.CharField(
        label="Nombre del dueño",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "bookstore-owner-name",
                "placeholder": "Nombre del dueño",
                "required": "True",
            }
        ),
    )
    email = forms.CharField(
        label="Direccion de la libreria",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "bookstore-adress",
                "placeholder": "adress",
                "required": "True",
            }
        ),
    )

    class Meta:
        model = BookStore
        fields = ["name", "owner", "adress"]