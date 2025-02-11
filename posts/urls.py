from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('studies/', views.studies, name='studies'),
    path('posts/', views.posts, name='posts'),
    path('contact/', views.contact, name='contact'),
]
