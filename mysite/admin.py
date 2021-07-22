from django.contrib import admin
from .models import User, Project, Profile, Review

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Review)