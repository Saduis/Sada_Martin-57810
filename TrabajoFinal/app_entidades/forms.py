from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class LibroForm (forms.Form):
    nombre= forms.CharField(max_length=100, required=True, label="Título")
    autor= forms.CharField(max_length=50, required=True, label="Autor")
    anio_edicion= forms.IntegerField( required=False, label="Año de edicion")
    editorial= forms.CharField(max_length=50, required=False, label="Editorial")

class AutorForm (forms.Form):
    nombre = forms.CharField(max_length=50, required=True, label="Nombre")
    apellido = forms.CharField(max_length=50, required=True, label="Apellido")
    nacionalidad = forms.CharField(max_length=50, required=True, label="Nacionalidad")

class LectorForm (forms.Form):
    nombre = forms.CharField(max_length=50, required=True, label="Nombre")
    apellido = forms.CharField(max_length=50, required=True, label="Apellido")
    email = forms.EmailField(required=False)

class PrestamoForm (forms.Form):
    nombre= forms.CharField(max_length=100, required=True, label="Nombre")
    apellido= forms.CharField(max_length=50, required=True, label="Apellido")
    libro= forms.CharField(max_length=50, required=True, label="Libro")
    fecha_prestamo= forms.DateField( required=True, label="Fecha préstamo")
    fecha_devolucion= forms.DateField( required=False,  label="Fecha devolución")

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Contraseña a confirmar", widget=forms.PasswordInput)

    class Meta :
        model = User
        fields = ["username","first_name", "last_name","email", "password1", "password2" ]

class UserEditForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido", max_length=50, required=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name","email" ]

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)