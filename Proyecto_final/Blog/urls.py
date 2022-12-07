from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls import reverse_lazy

from Blog import views
 
app_name = "Blog"
urlpatterns = [
    path("", views.index, name="home"),
    path("search/", views.search, name="search"),
    path('avatar/load', views.avatar_load, name='avatar-load'),
    path("libros_venta", views.libros_ventaListView.as_view(), name="libros_venta-list"),
    path("libros_venta/add/", views.libros_ventaCreateView.as_view(), name="libros_venta-add"),
    path("libros_venta/<int:pk>/detail/", views.libros_ventaDetailView.as_view(), name="libros_venta-detail"),
    path("libros_venta/<int:pk>/update/", views.libros_ventaUpdateView.as_view(), name="libros_venta-update"),
    path("libros_venta/<int:pk>/delete/", views.libros_ventaDeleteView.as_view(), name="libros_venta-delete"),
]