from django.urls import path

from bookstore import views
from Blog.views import bookstore
from bookstore.views import BookStoreCreateView, BookStoreDeleteView, BookStoreForm,BookStoreDetailView,BookStoreUpdateView

app_name = "bookstore"
urlpatterns = [
    path("bookstore", views.BookStoreListView.as_view(), name="bookstore-list"),
    path("bookstore/add/", views.BookStoreCreateView.as_view(), name="bookstore-add"),
    path("bookstore/<int:pk>/detail/", views.BookStoreDetailView.as_view(), name="bookstore-detail"),
    path("bookstore/<int:pk>/update/", views.BookStoreDeleteView.as_view(), name="bookstore-update"),
    path("bookstore/<int:pk>/delete/", views.BookStoreCreateView.as_view(), name="bookstore-delete"),
    path("bookstore/", bookstore)
]