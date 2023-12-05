from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,get_object_or_404 ,redirect
from django.http import Http404
from .forms import BlogPostForm, ProductoForm, BodegaForm, MovimientoForm, LoginForm
from .models import BlogPost, User, Producto, Movimiento
from django.contrib.auth import authenticate, login, logout
#from google.cloud import storage
from .forms import RegistrationForm
from rest_framework import generics
from .serializers import BlogPostSerializer

from rest_framework.decorators import api_view, permission_classes 

from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPost
#DRF
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

def is_user_auth_for_greeting(request):
    if request.user.is_authenticated:
        user_greeting = f"Hola, {request.user.username}" 
        return user_greeting
    return None

def index_albumes(request):
    user_greeting = is_user_auth_for_greeting(request)  # Variable para almacenar el saludo del usuario
    latest_post_list = None
    if user_greeting:
        latest_post_list = BlogPost.objects.order_by("-published_date")[:5]  
    template = loader.get_template("albumes/index.html")
    context = {
        "latest_post_list": latest_post_list,
        "user_greeting": user_greeting, #Si user greeting is none desde front obligamos a generar la vista de los botones
    }
    return HttpResponse(template.render(context, request))

def imagenes(request):
    user_greeting = is_user_auth_for_greeting(request)  # Variable para almacenar el saludo del usuario

##    # Recupera las URL de las imágenes de tu bucket de GCS
##
##    # Configura las credenciales (asegúrate de tener el archivo JSON de credenciales)
#    storage_client = storage.Client.from_service_account_json('credentials.json')
##
##    # Nombre del bucket y prefijo (si es necesario)
#    bucket_name = 'nombre-del-bucket'
#    prefix = 'carpeta/'
##
##    # Lista de imágenes en el bucket
#    blobs = storage_client.list_blobs(bucket_name, prefix=prefix)
##
##    # Obtén las URL de las imágenes
#    image_urls = [f"https://storage.googleapis.com/{bucket_name}/{blob.name}" for blob in blobs]
#
#    # Imprime las URLs de las imágenes
#    for url in image_urls:
#        print(url)
#        context = {
#            'image_urls': image_urls,
#        }
#
    return render(request, 'albumes/imagenes.html',{"user_greeting":user_greeting})    #, context)

def create_post(request):
    user_greeting = is_user_auth_for_greeting(request)  # Variable para almacenar el saludo del usuario
    if user_greeting:
        if request.method == 'POST':
            form = BlogPostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('blog:index_albumes')  # Cambia 'blog:index' a la URL de tu página de blog
        else:
            form = BlogPostForm()
    else :
        form = None
    return render(request, 'albumes/crear_post.html', {'form': form, 'user_greeting': user_greeting})


def create_product(request):
    user_greeting = is_user_auth_for_greeting(request)  # Variable para almacenar el saludo del usuario
    if user_greeting:
        if request.method == 'POST':
            form = ProductoForm(request.POST)
            if form.is_valid():
                prod = form.save(commit=False)
                prod.author = request.user
                prod.save()
                return redirect('blog:index_albumes')  # Cambia 'blog:index' a la URL de tu página de blog
        else:
            form = ProductoForm()
    else : 
        form = None
    return render(request, 'albumes/crear_producto.html', {'form': form, 'user_greeting': user_greeting})

def create_bodega(request):
    user_greeting = is_user_auth_for_greeting(request)  # Variable para almacenar el saludo del usuario
    if user_greeting:   
        if request.method == 'POST':
            form = BodegaForm(request.POST)
            if form.is_valid():
                prod = form.save(commit=False)
                prod.author = request.user
                prod.save()
                return redirect('blog:index_albumes')  # Cambia 'blog:index' a la URL de tu página de blog
        else:
            form = BodegaForm()
    else:
        form = None
    return render(request, 'albumes/crear_bodega.html', {'form': form, 'user_greeting': user_greeting})

def index_movs(request):
    user_greeting = is_user_auth_for_greeting(request)  # Variable para almacenar el saludo del usuario
    latest_mov_list = None
    if user_greeting:
        latest_mov_list = Movimiento.objects.all
    template = loader.get_template("albumes/index_movs.html")
    context = {
        "latest_mov_list": latest_mov_list,
        "user_greeting": user_greeting, #Si user greeting is none desde front obligamos a generar la vista de los botones
    }
    return HttpResponse(template.render(context, request))

def create_movimiento(request):
    user_greeting = is_user_auth_for_greeting(request)  # Variable para almacenar el saludo del usuario
    if user_greeting:
        if request.method == 'POST':
            form = MovimientoForm(request.POST)
            if form.is_valid():
                prod = form.save(commit=False)
                prod.author = request.user
                prod.save()
                return redirect('blog:index_albumes')  # Cambia 'blog:index' a la URL de tu página de blog
        else:
            form = MovimientoForm()
    else:
        form = None
    return render(request, 'albumes/crear_movimiento.html', {'form': form, 'user_greeting': user_greeting})



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)  # Pasar request como primer argumento para manejar la autenticación
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(f"Username{request.POST['username']}")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['Tema'] = "dark"
                request.session['user_id'] = user.id
                request.session['user_name'] = user.username
                print(f"Username{request.POST['username']}")
                userr_id = request.session.get("user_id")
                usrname = request.session.get("username")
                print(userr_id)
                print(username)

                # Redirige al usuario a la página deseada después del inicio de sesión.
                # Puedes personalizar esta parte según tus necesidades.
                return redirect('blog:index_albumes')
            else:
                # Manejar la lógica si la autenticación falla
                pass
    else:
        form = LoginForm()
    return render(request, 'albumes/login.html', {'form': form})

def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('blog:aboutus')  # Redirige al usuario a la página deseada después de cerrar sesión


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige al usuario a la página de inicio de sesión o a donde desees.
            return redirect('blog:login')  # Cambia 'login' por el nombre de tu vista de inicio de sesión
    else:
        form = RegistrationForm()
    return render(request, 'albumes/register.html', {'form': form})



def detail(request, post_id):
    user_greeting = is_user_auth_for_greeting(request)  # Variable para almacenar el saludo del usuario
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, "albumes/detail.html", {'post': post, 'user_greeting': user_greeting})

def index_prods(request):
    user_greeting = is_user_auth_for_greeting(request)  # Variable para almacenar el saludo del usuario
    latest_prod_list = None
    if user_greeting:
        latest_prod_list = Producto.objects.all
    template = loader.get_template("albumes/index_prods.html")
    context = {
        "latest_prod_list": latest_prod_list,
        "user_greeting": user_greeting, #Si user greeting is none desde front obligamos a generar la vista de los botones
    }
    return HttpResponse(template.render(context, request))

def detail_prod(request, producto_id):
    user_greeting = is_user_auth_for_greeting(request)  # Variable para almacenar el saludo del usuario
    prod = get_object_or_404(Producto, pk=producto_id)
    return render(request, "albumes/detail_prods.html", {'prod': prod, 'user_greeting': user_greeting})



def aboutus(request):
    user_greeting = is_user_auth_for_greeting(request)  # Variable para almacenar el saludo del usuario
    return render(request, 'albumes/aboutus.html',{"user_greeting":user_greeting})  # Renderiza tu página de inicio de sesión

def results(request, question_id):
    response = "You're looking at the results of post %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on post %s." % question_id)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])  # Añade la autenticación requerida
def posts_list(request):
    if request.method == 'GET':
        books = BlogPost.objects.all()
        serializer = BlogPostSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def posts_detail(request, pk):
    try:
        book = BlogPost.objects.get(pk=pk)
    except BlogPost.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = BlogPostSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BlogPostSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=204)


@api_view(['POST'])
@permission_classes([AllowAny])
def obtener_token(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if username is None or password is None:
        return Response({'error': 'Se requieren los campos "username" y "password".'}, status=400)

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'error': 'Credenciales inválidas.'}, status=400)

    if not user.check_password(password):
        return Response({'error': 'Credenciales inválidas.'}, status=400)

    # Generar tokens
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    return Response(
    {
        'access_token': access_token,
        'refresh_token': str(refresh)
    })
