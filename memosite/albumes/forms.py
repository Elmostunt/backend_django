from django import forms
from .models import BlogPost, Movimiento, DetalleMovimiento,Bodega,Producto
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

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
        
class LoginForm(AuthenticationForm):
    class Meta:
        fields = '__all__'  # Puedes especificar los campos que desees incluir en el formulario





class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']