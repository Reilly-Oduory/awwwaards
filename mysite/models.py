from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

# Create your models here.

class User(AbstractUser):
    pass

class Profile(models.Model):
    bio = models.TextField()
    d_o_b = models.DateField()

class Project(models.Model):
    description = models.TextField()
    slug = models.SlugField(max_length=15)
    url = models.CharField(max_length=60)
    user = models.ForeignKey(User, on_delete=CASCADE)

class Review(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    slug = models.SlugField(max_length=30)
    user = models.ForeignKey(User, on_delete=CASCADE)
