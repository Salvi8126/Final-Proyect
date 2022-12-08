"""Proyecto_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from Blog.views import index, Libros, VRegistro, about, bookstore
from Blog import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "bookstore"
urlpatterns = [
    path('accounts/',include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path("", index),
    path("post.html/", Libros),
    path("about.html", about),
    #path("salir/",  views.salir , name="salir"),
    path("login.html", VRegistro.as_view(), name="Auteticacion"),
    path("bookstore.html/", bookstore),
    path("bookstore/", include("bookstore.urls")),
    path("employees/", include("employees.urls")),
    path("Blog/", include("Blog.urls")),
]



