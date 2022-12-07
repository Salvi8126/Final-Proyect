from django import forms

from employees.models import Employee

from django import forms

from employees.models import Employee

class EmployeesForms(forms.ModelForm):
    name = forms.CharField(
        label="Nombre del empleado",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "employee-name",
                "placeholder": "Nombre del empleado",
                "required": "True",
            }
        ),
    )
    last_name = forms.CharField(
        label="Apellido del empleado",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "bookstore-last-name",
                "placeholder": "Apellido del empleado",
                "required": "True",
            }
        ),
    )
    adress = forms.CharField(
        label="Direccion del empleado",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "employees-adress",
                "placeholder": "adress",
                "required": "True",
            }
        ),
    )
    birth_date = forms.DateField(
        label="Fecha de nacimiento",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "employees-birth-date",
                "placeholder": "Fecha de nacimiento",
                "required": "True",
            }
        ),
    )

    class Meta:
        model = Employee
        fields = ["name", "last_name", "adress", "birth_date"]