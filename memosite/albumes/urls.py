from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index_albumes, name="index_albumes"), ##Aca muestro los POST por DJANGO
    path("productos", views.index_prods, name="index_prods"),
    path("movimientos", views.index_movs, name="index_movs"),

    # ex: /albumes/5/
    path("<int:post_id>/", views.detail, name="detail"), ##Aca muestro los DETALLES POST por DJANGO
    path("productos/<int:producto_id>/", views.detail_prod, name="detail_prod"),
    path("imagenes",views.imagenes,name="imagenes"),
    path('crear_post', views.create_post),
    path('crear_producto', views.create_product),
    path('crear_bodega', views.create_bodega),
    path('crear_movimiento', views.create_movimiento),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('register', views.register_view, name="register"),   
    path('about',views.aboutus, name="aboutus"),
    

    ##ACA PONDRE LOS REST FRAMEWORK, desde la ppt los copio, pego y cambio nomrbe de objeto del modelo que manejare
    ## Despues me voy al del proyecto validando que estan lo de las url
    path('postsapi/', views.posts_list, name='posts-list'),
    path('postsapi/<int:pk>/', views.posts_detail, name='posts-detail'),
    ##URL PARA TOKENS
    path('postsapi/obtener-token/', views.obtener_token, name='obtener-token'), 
]