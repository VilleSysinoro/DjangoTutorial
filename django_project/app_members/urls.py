from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='app_members'),
]