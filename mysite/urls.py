from django.urls import path
from . import views

urlpatterns = [
    path('api-overview/', views.apiOverview, name='api-overview'),
]
