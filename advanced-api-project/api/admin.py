from django.contrib import admin
from .models import Book , Author
# Register your models here.
# I had to register this models in my admin.py so as to be able to view them in my website.

admin.site.register(Book)
admin.site.register(Author)