from django.http import HttpResponse
from .models import Project, ReservarHora, Producto
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CrearNuevaReservaForm, CreateNewProyectForm, CustomUserLoginForm, CustomUserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from datetime import datetime

#Restapi

import rest_framework
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import ReservarHora
from .serializers import ReservarHoraSerializer

# Create your views here.


def index(request):
    title = 'Clínica INCclinic'
    return render(request, 'index.html', {
        'title': title
    })


def about(request):
    username = 'pablo'
    return render(request, "about.html", {
        'username': username
    })


def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" % username)


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })


def reservarhora(request):
    # get_object_or_404(ReservarHora, title=title)
    reservarhora = ReservarHora.objects.all()
    return render(request, 'reservarhora.html', {
        'reservarhora': reservarhora
    })


def crear_reserva(request):
    if request.method == 'POST':
        form = CrearNuevaReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservarhora')
    else:
        form = CrearNuevaReservaForm()
    return render(request, 'crear_reserva.html', {'form': form})

def create_project(request):
    if request.method == 'POST':
        form = CreateNewProyectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = CreateNewProyectForm()
    return render(request, 'create_project.html', {'form': form})


def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    reservarhora = ReservarHora.objects.filter(project_id=id)
    return render(request, 'detail.html', {
        'project': project,
        'reservarhoras': reservarhora
    })



class ProductoListView(ListView):
    model = Producto
    template_name = 'producto_list.html'

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'producto_detail.html'

class ProductoCreateView(CreateView):
    model = Producto
    template_name = 'producto_form.html'
    fields = ['nombre', 'descripcion', 'categoria']

class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = 'producto_form.html'
    fields = ['nombre', 'descripcion', 'categoria']

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'producto_confirm_delete.html'
    success_url = '/productos/'



def some_view(request):
    if 'is_active' in request.session:
        # El usuario ya ha iniciado sesión antes
        is_active = request.session['is_active']
    else:
        # Este es el primer inicio de sesión
        request.session['is_active'] = True


# views.py

def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserLoginForm(request)
    return render(request, 'login.html', {'form': form})



def logout_view(request):
    hora_cierre_sesion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    request.session['hora_cierre_sesion'] = hora_cierre_sesion
    print(f"La sesión fue cerrada a las {hora_cierre_sesion}") #Muestra en consola a que hora el usuario cierra la sesión :)
    logout(request)
    return redirect('index')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


#Restapi

@api_view(['GET', 'POST'])
def reservarhora_listapi(request):
    if request.method == 'GET':
        ReservarHora = ReservarHora.objects.all()
        serializer = ReservarHoraSerializer(ReservarHora, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReservarHoraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
