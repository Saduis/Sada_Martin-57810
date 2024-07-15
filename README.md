# Préstamos de libros

El objetivo de la web es tener un repositorio de libros de diferentes autores para conocerlos. Al mismo tiempo tener cierta información de cada autor y de los lectores que
se inscriban en la página. Por último tener un registro de quién tomó el préstamo. Las funcionalidades todavía están en desarrollo, por el momento solo se visualizan las diferentes
páginas pero no se relacionan entre ellas.

## Descripción

El proyecto fue escrito en python usando Django como framework. Se enmarca en el curso de Python de CoderHouse (https://www.coderhouse.com/) de la Comisión 57810 y es el trabajo final
para dicho curso.

## Visuales

Pagina inicial que permite loguearse o crear usuario para luego poder navegar hacia las diferentes secciones:
![image](https://github.com/user-attachments/assets/4aa3d527-dc05-43fd-a100-bd3467ed37cd)

## Empezando 🚀

Para bajar y ejecutar el proyecto seguir los siguientes pasos:

- $ git clone https://github.com/Saduis/Sada_Martin-57810.git
- $ cd ../Sada_Martin-57810/TrabajoFinal
- $ python manage.py runserver

## Usuarios de prueba ⚙️
Usuarios de prueba creados
- User: admin
- Password: admin
- ---------
- User: userPruebaEntrega
- Password: pass54321

## Ejecutando las Pruebas ⚙️
- Registrarse: permite crear un usuario
- Loguin: con usuario creado permite ingresar al sistema
- Inicio: se puede navegar hacia las diferentes secciones
- Libros (localhost/libros/): en dicha sección se visualizan los libros cargados. Cuenta con un ícono de búsqueda ![image](https://github.com/Saduis/Tercera_pre_entrega-SADA/assets/174150325/7d95c30a-7898-49be-b2b0-432ee9bdb1ec)
  (localhost/buscarLibros/) y uno para agregado de elementos ![image](https://github.com/Saduis/Tercera_pre_entrega-SADA/assets/174150325/473872bb-b3ac-4b37-a6dc-d02dbf166f37) (localhost/libroForm/)
- Autores (localhost/autores/): en dicha sección se visualizan los autores cargados. Cuenta con un ícono para agregado de elementos ![image](https://github.com/Saduis/Tercera_pre_entrega-SADA/assets/174150325/473872bb-b3ac-4b37-a6dc-d02dbf166f37) (localhost/autorForm/)
- Lectores (localhost/lectores/): en dicha sección se visualizan los autores cargados. Cuenta con un ícono para agregado de elementos ![image](https://github.com/Saduis/Tercera_pre_entrega-SADA/assets/174150325/473872bb-b3ac-4b37-a6dc-d02dbf166f37) (localhost/lectorForm/)
- Prestamos (localhost/prestamos/): en dicha sección se visualizan los autores cargados. Cuenta con un ícono para agregado de elementos ![image](https://github.com/Saduis/Tercera_pre_entrega-SADA/assets/174150325/473872bb-b3ac-4b37-a6dc-d02dbf166f37) (localhost/prestamoForm/)

## Construido Con 🛠️

- [Python](https://www.python.org/) - El lenguaje utilizado
- [Django](https://www.djangoproject.com/) - El framework web utilizado
- [Sqlite](https://www.sqlite.org/) - Sistema de base de datos

## Autores ✒️

- **Martin Sada** - https://github.com/Saduis
