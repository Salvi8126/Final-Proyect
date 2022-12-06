from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from bookstore.models import BookStore
from bookstore.forms import BookStoreForm



class BookStoreDetailView(DetailView):
    model = BookStore
    fields = ["name", "owner", "adress"]


class BookStoreCreateView(LoginRequiredMixin, CreateView):
    model = BookStore
    success_url = reverse_lazy("bookstore:bookstore-list")

    form_class = BookStoreForm

    def form_valid(self, form):
        """Filter to avoid duplicate students"""
        data = form.cleaned_data
        actual_objects = BookStore.objects.filter(
            name=data["name"],
            owner=data["owner"],
            adress=data["adress"],
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"La libreria {data['name']} | {data['adress']} | del dueño {data['owner']} ya está creada",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Libreria: {data['name']} - {data['adress']}. Creado exitosamente!",
            )
            return super().form_valid(form)


class BookStoreUpdateView(LoginRequiredMixin, UpdateView):
    model = BookStore
    fields = ["name", "owner", "adress"]

    def get_success_url(self):
        bookstore_id = self.kwargs["pk"]
        return reverse_lazy("bookstore:bookstore-detail", kwargs={"pk": bookstore_id})


class BookStoreDeleteView(LoginRequiredMixin, DeleteView):
    model = BookStore
    success_url = reverse_lazy("bookstore:bookstore-list")

class BookStoreListView(ListView):
    model = BookStore
    paginate_by = 3


