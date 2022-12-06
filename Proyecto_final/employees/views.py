from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from employees.models import Employee
from employees.forms import EmployeesForms


class EmployeesListView(ListView):
    model = Employee
    paginate_by = 3


class EmployeesDetailView(DetailView):
    model = Employee
    fields = ["name", "last_name", "birth_date", "adress"]


class EmployeesCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    success_url = reverse_lazy("employees:employees-list")

    form_class = EmployeesForms

    def form_valid(self, form):
        """Filter to avoid duplicate Employees"""
        data = form.cleaned_data
        actual_objects = Employee.objects.filter(
            name=data["name"],
            owner=data["last_name"],
            adress=data["adress"],
            birth_date=data["birth_date"],
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El empleado {data['name']} {data['last_name']} | {data['adress']} {data['birth_date']} ya está creada",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Empleado: {data['name']} - {data['last-name']}. Creado exitosamente!",
            )
            return super().form_valid(form)


class EmployeesUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee
    fields = ["name", "last_name", "birth_date", "adress"]

    def get_success_url(self):
        Employees_id = self.kwargs["pk"]
        return reverse_lazy("employees:employees-detail", kwargs={"pk": Employees_id})


class EmployeesDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    success_url = reverse_lazy("employees:employees-list")