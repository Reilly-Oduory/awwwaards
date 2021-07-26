from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import messages
from .forms import RegistrationForm, CreateProfileForm, UpdateProfileForm, CreateProjectForm, UpdateProjectForm, ReviewProjectForm
from .serializers import ProfileSerializer, ProjectSerializer
from .models import User, Profile, Project, Review

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
        'user-specific-profile' : '/<user>/profile/',
        'create-profile' : '/create-profile/',
        'update-profile' : '/update-profile/',

        # projects
        'project-list' : '/projects/',
        'user-project-list' : '<user>/projects/',
        'single-project' : '<user>/<pk>/',
        'create-project' : '<user>/create/project/',
        'update-project' : '<user>/profile/<pk>/update/',
        'delete-project' : '<user>/profile/<pk>/delete/',

    }
    return Response(api_urls)

@api_view(['GET'])
def ProfileList(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def UserProfile(request, user_id):
    user = User.objects.filter(id=user_id).first()
    profile = Profile.objects.filter(user=user).first()
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)

@api_view(['POST'])
def CreateUserProfile(request):
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
    
    return Response(serializer.data)

@api_view(['POST'])
def UpdateUserProfile(request):
    profile = Profile.objects.filter(user=request.user).first()
    serializer = ProfileSerializer(instance=profile, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def ProjectList(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def UserProjects(request):
    projects = Project.objects.filter(user=request.user).all()
    serializer = ProjectSerializer(projects, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def SingleProject(request, pk):
    project = Project.objects.filter(id=pk).first()
    serializer = ProjectSerializer(project)

    return Response(serializer.data)

@api_view(['POST'])
def CreateProject(request):
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
    
    return Response(serializer.data) 

@api_view(['POST'])
def UpdateProject(request, pk):
    project = Project.objects.filter(id=pk).first()
    serializer = ProjectSerializer(instance=project, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteProject(request, pk):
    project = Project.objects.filter(id=pk).first()
    project.delete()

    return Response("Project deleted")



# user views
def index(request):
    title = 'Nice test'
    context = {
        "title":title,
    }

    return render(request, 'index.html', context)

@login_required(login_url='/login/')
def profileView(request):
    profile = Profile.objects.filter(user=request.user).first()
    projects = Project.objects.filter(user=request.user).all()
    context = {
        "profile":profile,
        "projects":projects,
    }

    return render(request, 'profile/profile.html', context)

@login_required(login_url='/login/')
def projectView(request, pk):
    project = Project.objects.filter(id=pk).first()
    reviews = Review.objects.filter(project=pk).all()
    context = {
        "project":project,
        "reviews":reviews
    }
    return render(request, 'project/project-view.html', context)

@login_required(login_url='/login/')
def createProject(request):
    form = CreateProjectForm()
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect(f'/profile/')

    context = {"form":form}

    return render(request, 'personal/create-project.html')

@login_required(login_url='/login/')
def reviewProject(request, project_id):
    project = Project.objects.filter(id=project_id).first()
    form = ReviewProjectForm()
    if request.method == 'POST':
        form = ReviewProjectForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.project = project
            obj.user = request.user
            obj.save()
            return redirect(f'/project/{project_id}/')

    context = {
        "form":form,
        "project":project
    }

    return render(request, 'review/review.html', context)

@login_required(login_url='/login/')
def updateProject(request, project_id):
    project = Project.objects.get(id=project_id)
    form = UpdateProjectForm()
    if request.method == 'POST':
        form = UpdateProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect(f'/project/{project_id}/')

    context = {
        "form":form,
        "project":project
    }

    return render(request, 'personal/update-project.html', context)

@login_required(login_url='/login/')
def createProfile(request):
    form = CreateProfileForm( )
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect(f'/profile/')
    context = {
        "form":form
    }

    return render(request, 'profile/create-profile.html', context)

@login_required(login_url='/login/')
def updateProfile(request):
    profile = Profile.objects.get(user=request.user)
    form = UpdateProfileForm()
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(f'/profile/')

    context = {
        "form":form,
    }

    return render(request, 'profile/update-profile.html', context)

@login_required(login_url='/login/')
def deleteProject(request, project_id):
    project = Project.objects.get(id=project_id)
    project.del_project()
    context = {
        "project":project
    }

    return render(request, 'personal/delete-project.html', context)
