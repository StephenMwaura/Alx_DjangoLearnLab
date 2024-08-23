from django.db import models 



# from django.db.models.signals import post_save
# from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser , BaseUserManager
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title , self.author
    class Meta():
        permissions = [
            ('can_add_book', "can add book"),
            ('can_change_book'," can change book"),
            ('can_delete_book', "can delete book"),
        ]
    
    
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    def __str__(self):
        return {self.name}, {self.books}
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    def __str__(self):
        return {self.name} , {self.library}

class UserProfile(models.Model):
    # user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    role_choices = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),

    ]
role = models.CharField(max_length=20, choices='role_choices')

def user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()

# # from  django.contrib.auth.decorators import user_passes_test
# # from django.http import HttpResponse

# # def is_Admin(user):
# #     return user.is_authenticated and user.groups.filter(name='Admin').exists()
# # @user_passes_test(is_Admin)
# # def Admin_view(request):
# #     return HttpResponse("Welcome, Admin")

