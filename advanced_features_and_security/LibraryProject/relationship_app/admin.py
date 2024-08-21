from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin 

# Register your models here.

# class ModelAdmin(UserAdmin):
#     model = CustomUser

#     list_display = ('username', 'email', 'date_of_birth', 'is_staff')

# admin.site.register(CustomUser ,ModelAdmin)