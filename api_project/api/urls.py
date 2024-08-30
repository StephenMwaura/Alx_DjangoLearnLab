from django.urls import path
from views import BookList

urlpatterns = [
    path("api.urls", views.BookList.as_view(), name="book_list_view"),

]
