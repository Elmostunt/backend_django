from django.db import models
from django.contrib.auth.models import User

# Modelo para las categorías de mascotas
class PetCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Modelo para las mascotas
class Pet(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(PetCategory, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    description = models.TextField()
    #image = models.ImageField(upload_to='pets/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Modelo para las entradas del blog
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    pets_related = models.ManyToManyField(Pet, blank=True)

    def __str__(self):
        return self.title
    
class Bodega(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100, default='Valor predeterminado')
    jefe_bodega = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

    def stock_producto(self, producto):
        return self.productos.filter(id=producto.id).count()

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    bodegas = models.ManyToManyField(Bodega, related_name='productos')

    def __str__(self):
        return self.nombre
    

class Movimiento(models.Model):
    bodega_origen = models.ForeignKey(Bodega, on_delete=models.CASCADE, related_name='movimientos_salida')
    bodega_destino = models.ForeignKey(Bodega, on_delete=models.CASCADE, related_name='movimientos_entrada')
    productos = models.ManyToManyField(Producto, through='DetalleMovimiento')
    #usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    
class DetalleMovimiento(models.Model):
    movimiento = models.ForeignKey(Movimiento, on_delete=models.CASCADE, blank=True, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)
