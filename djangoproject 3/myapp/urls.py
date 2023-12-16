from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path ('about/', views.about, name="about"),
    path('hello/<str:username>', views.hello, name="hello"),
    path('projects/', views.projects, name="projects"),
    path('projects/<int:id>', views.project_detail, name="project_detail"),
    path('reservarhora/', views.reservarhora, name="reservarhora"),
    path('crear_reserva/', views.crear_reserva, name="crear_reserva"),
    path('create_project/', views.create_project, name="create_project"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('api/', views.reservarhora_listapi, name='api_reservarhora'),
]   