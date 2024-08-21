from django.db import models
from django.conf import settings
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
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True , blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/')

    def __str__(self):
        return self.username
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["date_of_birth" ,"profile_photo"]


    

class UserManager(BaseUserManager):
    def create_user(self,username,  date_of_birth , profile_photo, password=None):
        if not username:
            raise ValueError("The Username field must be set")
        if not date_of_birth:
            raise ValueError("User must enter date of birth")
        if not profile_photo:
            raise ValueError("User must place profile photo")
        user = self.model(
        username = username,
        date_of_birth = date_of_birth,
        profile_photo = profile_photo
    )
        user.set_password(password)
        user.save(using=self._db)
    def create_superuser(self,username, date_of_birth, profile_photo, password =None):
        user = self.create_user( username,date_of_birth, profile_photo, password =None)
        user._is_admin = True
        user.is_staff =True

        user.is_superuser = True
        user.save(using= self._db)
        return user