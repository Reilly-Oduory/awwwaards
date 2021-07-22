from django.db.models import fields
from .models import User, Profile, Project
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class meta:
        model = User
        fields = '__all__'

class ProfileSerialer(serializers.ModelSerializer):
    class meta:
        model = Profile
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
