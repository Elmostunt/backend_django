from django import forms
from .models import BlogPost, Movimiento, User, DetalleMovimiento,Bodega,Producto
from django.contrib.auth.forms import UserCreationForm


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'pets_related']  # Especifica los campos que deseas incluir en el formulario

        
class MovimientoForm(forms.ModelForm):
    class Meta:
        model = Movimiento
        fields = ('bodega_origen', 'bodega_destino', 'productos',)


class DetalleMovimientoForm(forms.ModelForm):
    class Meta:
        model = DetalleMovimiento
        fields = '__all__'
        
class ProductoForm(forms.ModelForm):
    bodega = forms.ModelChoiceField(queryset=Bodega.objects.all())
    class Meta:
        model = Producto
        #fields = ('nombre', 'descripcion', 'bodega')
        #fields = ('nombre', 'descripcion')
        fields = '__all__'

class BodegaForm(forms.ModelForm):
    class Meta:
        model = Bodega
        fields = '__all__'