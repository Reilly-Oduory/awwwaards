from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    # auth
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    # api
     # profile
    path('api-overview/', views.apiOverview, name='api-overview'),
    path('api/profiles/', views.ProfileList, name='api-profile-list'),
    path('api/<user_id>/profile/', views.UserProfile, name='api-user-specific-profile'),
    path('api/create-profile/', views.CreateUserProfile, name='api-create-profile'),
    path('api/update-profile/', views.UpdateUserProfile, name='api-update-profile'),

     # projects
    path('api/projects/', views.ProjectList, name='api-project-list'),
    path('api/user/projects/', views.UserProjects, name='api-user-project-list'),
    path('api/project/<pk>/', views.SingleProject, name='api-single-project'),
    path('api/create/project/', views.CreateProject, name='api-create-project'),
    path('api/update/project/<pk>/', views.UpdateProject, name='api-update-project'),
    path('api/delete/project/<pk>/', views.DeleteProject, name='api-delete-project'),

    # user
    path('', views.index, name='home'),
    #profile
    path('profile/', views.profileView, name='profile'),
    path('create/profile', views.createProfile, name='create-profile'),
    path('update/profile', views.updateProfile, name='update-profile'),

    #project
    path('project/<pk>/', views.projectView, name='single-project-view'),
    path('create/project/', views.createProject, name='create-project'),
    path('update/project/<project_id>', views.updateProject, name='update-project'),
    path('delete/project/<project_id>', views.deleteProject, name='delete-project'),
    path('create/project/review/', views.reviewProject, name='review-project')
]
