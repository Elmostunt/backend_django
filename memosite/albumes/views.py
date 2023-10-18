from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,get_object_or_404 ,redirect
from django.http import Http404
from .forms import BlogPostForm, ProductoForm, BodegaForm, MovimientoForm
from .models import BlogPost, User
from django.contrib.auth import authenticate, login
from google.cloud import storage




def index_albumes(request):
    latest_post_list = BlogPost.objects.order_by("-published_date")[:5]
    template = loader.get_template("albumes/index.html")
    context = {
        "latest_post_list": latest_post_list,
    }
    return HttpResponse(template.render(context, request))

def imagenes(request):
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
    return render(request, 'albumes/imagenes.html')    #, context)

def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:index_albumes')  # Cambia 'blog:index' a la URL de tu página de blog
    else:
        form = BlogPostForm()
    
    return render(request, 'albumes/crear_post.html', {'form': form})


def create_product(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.author = request.user
            prod.save()
            return redirect('blog:index_albumes')  # Cambia 'blog:index' a la URL de tu página de blog
    else:
        form = ProductoForm()
    
    return render(request, 'albumes/crear_producto.html', {'form': form})

def create_bodega(request):
    if request.method == 'POST':
        form = BodegaForm(request.POST)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.author = request.user
            prod.save()
            return redirect('blog:index_albumes')  # Cambia 'blog:index' a la URL de tu página de blog
    else:
        form = BodegaForm()
    
    return render(request, 'albumes/crear_bodega.html', {'form': form})

def create_movimiento(request):
    if request.method == 'POST':
        form = MovimientoForm(request.POST)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.author = request.user
            prod.save()
            return redirect('blog:index_albumes')  # Cambia 'blog:index' a la URL de tu página de blog
    else:
        form = MovimientoForm()
    
    return render(request, 'albumes/crear_movimiento.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #user = authenticate(request, username=username, password=password)
        user = None
        if user is not None:
            login(request, user)
            # Redirige al usuario a la página deseada después del inicio de sesión.
            # Puedes personalizar esta parte según tus necesidades.
            return redirect('blog:index_albumes')
        else:
            # Manejar la lógica si la autenticación falla
            pass
    return render(request, 'albumes/login.html')  # Renderiza tu página de inicio de sesión



def detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, "albumes/detail.html", {"post": post})



def aboutus(request):
    return render(request, 'albumes/aboutus.html')  # Renderiza tu página de inicio de sesión

def results(request, question_id):
    response = "You're looking at the results of post %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on post %s." % question_id)