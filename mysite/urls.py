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
    path('api/profiles/', views.ProfileList, name='profile-list'),
    path('api/<user_id>/profile', views.UserProfile, name='user-specific-profile'),
    path('api/create-profile', views.CreateUserProfile, name='create-profile'),
    path('api/update-profile', views.UpdateUserProfile, name='update-profile'),

     # projects
    path('api/projects/', views.ProjectList, name='project-list'),
    path('api/user/projects', views.UserProjects, name='user-project-list'),
    path('api/project/<pk>', views.SingleProject, name='single-project'),
    path('api/create/project', views.CreateProject, name='create-project'),
    path('api/update/project/<pk>', views.UpdateProject, name='update-project'),
    path('api/delete/project/<pk>', views.DeleteProject, name='delete-project'),

    # user
    path('', views.index, name='home')
]
