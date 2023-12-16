# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import ReservarHora, Project, User

class CrearNuevaReservaForm(forms.ModelForm):
    class Meta:
        model = ReservarHora
        fields = ['title', 'description', 'project']

class CreateNewProyectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(CreateNewProyectForm, self).__init__(*args, **kwargs)
        
class CustomAuthenticationForm(AuthenticationForm):
    # Personaliza el formulario de inicio de sesión si es necesario
    pass

class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Nombre de usuario',
        widget=forms.TextInput(attrs={'class': 'black-text'}),
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'black-text'}),
    )

    class Meta:
        model = User
        fields = ['username', 'password']

class CustomUserCreationForm(UserCreationForm):
    # Puedes personalizar este formulario según tus necesidades
    email = forms.EmailField(label='Correo electrónico')
    username = forms.CharField(label='Nombre de usuario')
    password1 = forms.CharField(label='Contraseña')
    password2 = forms.CharField(label='Confirmar contraseña')

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)