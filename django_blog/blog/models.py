
from django.db import models

from django.contrib.auth.models import  AbstractUser , BaseUserManager
from django.conf import settings
from django.db import models
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)


class CustomUserManager(BaseUserManager): # custom user manager inherits from the BaseUser
    def create_user(self , username, bio , photo, password=None):
        if not username: 
            raise ValueError("The username is required")
        user = self.model(
            username = username,
            bio = bio,
            photo = photo

        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, bio, photo, password=None):
        user = self.create_user(username,bio,photo,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser): # inherits from the abstract user
    bio = models.TextField(max_length=200)
    photo = models.ImageField(blank=True, null=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["bio", "photo"]

    objects = CustomUserManager()

    def __str__(self):
        return self.username

