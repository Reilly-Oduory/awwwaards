from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
# auth views

# api views
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        # profiles
        'profile-list' : '/profiles/',
        'user-specific-profile' : '/user/profile/',
        'update-profile' : '/<user>/<pk>/update/',

        # projects
        'project-list' : '/projects/',
        'user-project-list' : '<user>/projects/',
        'single-project' : '<user>/<pk>/',
        'create-project' : '<user>/create/project/',
        'update-project' : '<user>/profile/<pk>/update/',
        'delete-project' : '<user>/profile/<pk>/delete/',

    }
    return Response(api_urls)

# user views