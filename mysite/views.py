from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import messages
from .forms import RegistrationForm

# Create your views here.
# auth views
def register_user(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            messages.success(request, "You have successfully Signed Up")
            return redirect(f'/')
        
    context = {"form":form}
    return render(request, 'auth/register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in")
            return redirect(f'/')
        else:
            messages.info(request, "The Username or Password is incorrect")

    context = {}
    return render(request, 'auth/login.html', context)

login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/login')


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
def index(request):
    title = 'Nice test'
    context = {
        "title":title,
    }

    return render(request, 'index.html', context)