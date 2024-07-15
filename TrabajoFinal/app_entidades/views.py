from django.shortcuts import render, redirect
from django.views.generic  import ListView,CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from app_entidades.models import *
from app_entidades.forms import *

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin #Trabaja sobre las clases
from django.contrib.auth.decorators import login_required #Trabaja sobre las funciones

# Create your views here.

def home(request):
    return render(request, "entidades/index.html")

def acerca(request):
    return render(request, "entidades/acerca.html")


#__LIBROS

@login_required
def libros(request):
    contexto = {'libros': Libro.objects.all()}
    return render(request, "entidades/libros.html", contexto)

@login_required
def libroForm(request):
    if request.method == "POST":
        miForm = LibroForm(request.POST)
        if miForm.is_valid():
            nombre = miForm.cleaned_data.get("nombre")
            autor = miForm.cleaned_data.get("autor")
            anio_edicion = miForm.cleaned_data.get("anio_edicion")
            editorial = miForm.cleaned_data.get("editorial")

            libro = Libro(nombre=nombre, autor=autor, anio_edicion=anio_edicion, editorial=editorial) 
            libro.save()

            contexto = {"libros": Libro.objects.all()}

            return render(request, "entidades/libros.html", contexto)
    else:
        miForm = LibroForm()
    return render(request, "entidades/libroForm.html", {"form" : miForm})

@login_required
def buscarLibros(request):
    return render(request , "entidades/buscar.html") 

@login_required
def encontrarLibros(request):
    if request.GET["buscar"]:
        patron= request.GET["buscar"]
        libros = Libro.objects.filter(nombre__icontains=patron )
        contexto = {'libros': libros}
    else:
        contexto = {'libros' : Libro.objects.all()}
    return render(request, "entidades/libros.html", contexto)

@login_required
def libroUpdate(request, id_libro):
    libro = Libro.objects.get(id=id_libro)
    if request.method == "POST":
        miForm = LibroForm(request.POST)
        if miForm.is_valid():
            libro.nombre = miForm.cleaned_data.get("nombre")
            libro.autor = miForm.cleaned_data.get("autor")
            libro.anio_edicion = miForm.cleaned_data.get("anio_edicion")
            libro.editorial  = miForm.cleaned_data.get("editorial")
            
            libro.save()

            contexto = {"libros": Libro.objects.all()}

            return render(request, "entidades/libros.html", contexto)
    else:
        miForm = LibroForm(initial={"nombre":libro.nombre, "autor":libro.autor, "anio_edicion":libro.anio_edicion, "editorial":libro.editorial})
    
    return render(request, "entidades/libroForm.html", {"form": miForm})

class LibroDelete(LoginRequiredMixin, DeleteView):
    model = Libro
    success_url = reverse_lazy("libros")



#__AUTORES

@login_required
def autores(request):
    contexto = {'autores': Autor.objects.all()}
    return render(request, "entidades/autores.html", contexto)

@login_required
def autorForm(request):
    if request.method == "POST":
        miForm = AutorForm(request.POST)
        if miForm.is_valid():
            nombre = miForm.cleaned_data.get("nombre")
            apellido = miForm.cleaned_data.get("apellido")
            nacionalidad = miForm.cleaned_data.get("nacionalidad")

            autor = Autor(nombre=nombre, apellido=apellido, nacionalidad=nacionalidad)
            autor.save()

            contexto = {"autores": Autor.objects.all()}

            return render(request, "entidades/autores.html", contexto)

    else:
        miForm = AutorForm()
    return render(request, "entidades/autorForm.html", {"form":miForm})

@login_required
def buscarAutores(request):
    return render(request , "entidades/buscarAutores.html") 

@login_required
def encontrarAutores(request):
    if request.GET["buscar"]:
        patron= request.GET["buscar"]
        autores = Autor.objects.filter(apellido__icontains=patron )
        contexto = {'autores': autores}
    else:
        contexto = {'autores' : Autor.objects.all()}
    return render(request, "entidades/autores.html", contexto)

@login_required
def autorUpdate(request, id_autor):
    autor = Autor.objects.get(id=id_autor)
    if request.method == "POST":
        miForm = AutorForm(request.POST)
        if miForm.is_valid():
            autor.nombre = miForm.cleaned_data.get("nombre")
            autor.apellido = miForm.cleaned_data.get("apellido")
            autor.nacionalidad = miForm.cleaned_data.get("nacionalidad")
            
            autor.save()

            contexto = {"autores": Autor.objects.all()}

            return render(request, "entidades/autores.html", contexto)
    else:
        miForm = AutorForm(initial={"nombre":autor.nombre, "apellido":autor.apellido, "nacionalidad":autor.nacionalidad})
    
    return render(request, "entidades/autorForm.html", {"form": miForm})

class AutorDelete(LoginRequiredMixin, DeleteView):
    model = Autor
    success_url = reverse_lazy("autores")


    
#__LECTORES

@login_required
def lectores(request):
    contexto = {'lectores': Lector.objects.all()}
    return render(request, "entidades/lectores.html", contexto)

@login_required
def lectorForm(request):
    if request.method == "POST":
        miForm = LectorForm(request.POST)
        if miForm.is_valid():
            nombre = miForm.cleaned_data.get("nombre")
            apellido = miForm.cleaned_data.get("apellido")
            email = miForm.cleaned_data.get("email")

            lector = Lector(nombre=nombre, apellido=apellido, email=email)
            lector.save()

            contexto = {"lectores": Lector.objects.all()}

            return render(request, "entidades/lectores.html", contexto)

    else:
        miForm = LectorForm()
    return render(request, "entidades/lectorForm.html", {"form":miForm})

@login_required
def lectorUpdate(request, id_lector):
    lector = Lector.objects.get(id=id_lector)
    if request.method == "POST":
        miForm = LectorForm(request.POST)
        if miForm.is_valid():
            lector.nombre = miForm.cleaned_data.get("nombre")
            lector.apellido = miForm.cleaned_data.get("apellido")
            lector.email = miForm.cleaned_data.get("email")
            
            lector.save()

            contexto = {"lectores": Lector.objects.all()}

            return render(request, "entidades/lectores.html", contexto)
    else:
        miForm = LectorForm(initial={"nombre":lector.nombre, "apellido":lector.apellido, "email":lector.email})
    
    return render(request, "entidades/lectorForm.html", {"form": miForm})

@login_required
def lectorDelete(request, id_lector):
    lector = Lector.objects.get(id=id_lector)
    lector.delete()
    contexto = {"lectores": Lector.objects.all()}

    return render(request, "entidades/lectores.html", contexto)

@login_required
def buscarLectores(request):
    return render(request , "entidades/buscarLectores.html") 

@login_required
def encontrarLectores(request):
    if request.GET["buscar"]:
        patron= request.GET["buscar"]
        lectores = Lector.objects.filter(apellido__icontains=patron )
        contexto = {'lectores': lectores}
    else:
        contexto = {'lectores' : Lector.objects.all()}
    return render(request, "entidades/lectores.html", contexto)



#__PRESTAMOS

@login_required
def prestamos(request):
    contexto = {'prestamos': Prestamo.objects.all()}
    return render(request, "entidades/prestamos.html", contexto)

@login_required
def prestamoForm(request):

    if request.method == "POST":
        miForm = PrestamoForm(request.POST)
        if miForm.is_valid():
            nombre = miForm.cleaned_data.get("nombre")
            apellido = miForm.cleaned_data.get("apellido")
            libro = miForm.cleaned_data.get("libro")
            fecha_prestamo = miForm.cleaned_data.get("fecha_prestamo")
            fecha_devolucion = miForm.cleaned_data.get("fecha_devolucion")

            prestamo = Prestamo(nombre=nombre, apellido=apellido, libro=libro, fecha_prestamo=fecha_prestamo, fecha_devolucion=fecha_devolucion)
            prestamo.save()

            contexto = {"prestamos": Prestamo.objects.all()}

            return render(request, "entidades/prestamos.html", contexto)

    else:
        miForm = PrestamoForm()
    return render(request, "entidades/prestamoForm.html", {"form":miForm})

class PrestamoUpdate(LoginRequiredMixin, UpdateView):
    model = Prestamo
    fields = ["nombre","apellido","libro","fecha_prestamo","fecha_devolucion"]
   
    exclude = ("fecha_devolucion",)
   
    success_url = reverse_lazy("prestamos")

class PrestamoDelete(LoginRequiredMixin, DeleteView):
    model = Prestamo
    success_url = reverse_lazy("prestamos")

@login_required
def buscarPrestamos(request):
    return render(request , "entidades/buscarPrestamos.html") 

@login_required
def encontrarPrestamos(request):
    if request.GET["buscar"]:
        patron= request.GET["buscar"]
        prestamos = Prestamo.objects.filter(libro__icontains=patron )
        contexto = {'prestamos': prestamos}
    else:
        contexto = {'prestamos' : Prestamo.objects.all()}
    return render(request, "entidades/prestamos.html", contexto)


#__LOGIN/LOGOUT/REGISTRACION


def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
        #___Buscar avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar

            return render(request, "entidades/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
        miForm = AuthenticationForm()   
    return render(request, "entidades/login.html", {"form":miForm})


def registroUsuario(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            miForm.save()
            print("Usuario guardado")
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()

    return render(request, "entidades/registro.html", {"form":miForm})


#___EDICION DE PERFIL/AVATAR

@login_required
def editarProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.mail = miForm.cleaned_data.get("mail")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("home"))
    else:
        miForm = UserEditForm(instance=usuario)

    return render(request, "entidades/editarPerfil.html", {"form":miForm})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "entidades/cambiarClave.html"
    success_url = reverse_lazy("home")

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            #Se borran los avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len (avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #_________________
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()

            #_______Enviar la imagen a home
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            #___________________

            return redirect(reverse_lazy("home"))
    else:
        miForm = AvatarForm()

    return render(request, "entidades/agregar_avatar.html", {"form":miForm})



#___PRUEBA

class PrestamoList(LoginRequiredMixin, ListView):
    model = Prestamo

class PrestamoCreate(LoginRequiredMixin, CreateView):
    model = Prestamo
    fields = ["nombre","apellido","fecha_prestamo"]
    success_url = reverse_lazy("prestamos")


#class PrestamoUpdate(DeleteView):
    model = Prestamo
    success_url = reverse_lazy("prestamos")







