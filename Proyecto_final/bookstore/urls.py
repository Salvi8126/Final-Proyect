from django.urls import path

from bookstore import views
from Blog.views import bookstore

app_name = "bookstore"
urlpatterns = [
    path("bookstore", views.StudentListView.as_view(), name="bookstore-list"),
    path("bookstore/add/", views.StudentCreateView.as_view(), name="bookstore-add"),
    path("bookstore/<int:pk>/detail/", views.BookstoreDetailView.as_view(), name="bookstore-detail"),
    path("bookstore/<int:pk>/update/", views.BookstoreUpdateView.as_view(), name="bookstore-update"),
    path("bookstore/<int:pk>/delete/", views.BookstoreDeleteView.as_view(), name="bookstore-delete"),
    path("bookstore/", bookstore)
]