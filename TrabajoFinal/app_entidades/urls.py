from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name = "home"),
    path('acerca/', acerca, name = "acerca"),


    #__Libros
    path('libros/', libros, name = "libros"),
    path('libroForm/', libroForm, name = "libroForm"),
    path('buscarLibros', buscarLibros, name = "buscarLibros"),
    path('encontrarLibros', encontrarLibros, name = "encontrarLibros"),
    path('libroUpdate/<id_libro>',libroUpdate, name = "libroUpdate"),
    path('libroDelete/<int:pk>', LibroDelete.as_view(template_name = "entidades/libro_confirm_delete.html"), name = "libroDelete"),

    #__Autores
    path('autores/', autores, name = "autores"),
    path('autorForm/', autorForm, name = "autorForm"),
    path('buscarAutores', buscarAutores, name = "buscarAutores"),
    path('encontrarAutores', encontrarAutores, name = "encontrarAutores"),
    path('autorUpdate/<id_autor>',autorUpdate, name = "autorUpdate"),
    path('autorDelete/<int:pk>', AutorDelete.as_view(template_name = "entidades/autor_confirm_delete.html"), name = "autorDelete"),

    #__Lectores
    path('lectores/', lectores, name = "lectores"),
    path('lectorForm/', lectorForm, name = "lectorForm"),
    path('lectorUpdate/<id_lector>/', lectorUpdate, name="lectorUpdate"),
    path('lectorDelete/<id_lector>/', lectorDelete, name="lectorDelete"), 
    path('buscarLectores', buscarLectores, name = "buscarLectores"),
    path('encontrarLectores', encontrarLectores, name = "encontrarLectores"),

    #__Prestamos
    path('prestamos/', prestamos, name = "prestamos"),
    path('prestamoForm/', prestamoForm, name = "prestamoForm"),    
    path('prestamoUpdate/<int:pk>', PrestamoUpdate.as_view(template_name = "entidades/prestamo_form.html"), name = "prestamoUpdate"),
    path('prestamoDelete/<int:pk>', PrestamoDelete.as_view(template_name = "entidades/prestamo_confirm_delete.html"), name = "prestamoDelete"),
    path('buscarPrestamos', buscarPrestamos, name = "buscarPrestamos"),
    path('encontrarPrestamos', encontrarPrestamos, name = "encontrarPrestamos"),
   
    #__Login
    path ('login/', loginRequest, name="login"),
    path ('logout/', LogoutView.as_view(template_name="entidades/logout.html"), name = "logout"),
    path('registro/', registroUsuario, name="registro"),

    #__Edicion de Perfil
    path ('perfil/', editarProfile, name="perfil"),
    path ('<int:pk>/password/',CambiarClave.as_view() , name="cambiarClave"),
    path ('agregar_avatar/', agregarAvatar , name="agregar_avatar"),
    


    #__Pruebas de CBV
    #path('prestamosDelete/<int:pk>', PrestamoUpdate.as_view(), name = "prestamosUpdate"),
    #path('prestamoCreate/', PrestamoCreate.as_view(), name = "prestamoCreate"),


]
