from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
class Profile(models.Model):
    fullname = models.CharField(max_length=45, null=True)
    profile_pic = models.ImageField(upload_to = 'profile_photos/', null=True, blank=True)
    bio = models.TextField(null=True)
    d_o_b = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)

class Project(models.Model):
    project_pic = models.ImageField(upload_to = 'project_photos/', null=True, blank=True)
    description = models.TextField(null=True)
    url = models.CharField(max_length=60, null=True)
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)

class Review(models.Model):
    title = models.CharField(max_length=30, null=True)
    content = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)
