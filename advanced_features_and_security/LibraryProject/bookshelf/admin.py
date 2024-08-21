from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin 

# Register your models here.

class ModelAdmin(UserAdmin):
    model = CustomUser

    list_display = ('username', 'email', 'date_of_birth', 'is_staff')

admin.site.register(CustomUser ,ModelAdmin)


from .models import Book



class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('title' , 'author')
    search_fields = ('title', 'author')


admin.site.register(Book, BookAdmin)

class ModelAdmin(UserAdmin):
    model = CustomUser

    list_display = ('username', 'email', 'date_of_birth', 'is_staff')

admin.site.register(Book, BookAdmin ,CustomUser ,ModelAdmin)
