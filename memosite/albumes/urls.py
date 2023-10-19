from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index_albumes, name="index_albumes"),
    
    # ex: /albumes/5/
    path("<int:post_id>/", views.detail, name="detail"),
    path("imagenes",views.imagenes,name="imagenes"),
    path('crear_post', views.create_post),
    path('crear_producto', views.create_product),
    path('crear_bodega', views.create_bodega),
    path('crear_movimiento', views.create_movimiento),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('register', views.register_view, name="register"),   
    path('about',views.aboutus, name="aboutus")
]