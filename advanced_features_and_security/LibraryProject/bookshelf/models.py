from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} year {int(self.publication_year)}"
    
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True , blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/')

    def __str__(self):
        return self.username
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["date_of_birth" ,"profile_photo"]


    

class CustomUserManager(BaseUserManager):
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