from django.urls import path
from . import views

urlpatterns = [
    # auth
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    # api
    path('api-overview/', views.apiOverview, name='api-overview'),

    # user
    path('', views.index, name='home')
]
