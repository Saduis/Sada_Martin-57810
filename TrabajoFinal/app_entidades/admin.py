from django.contrib import admin

# Register your models here.

from app_entidades.models import *


class LectorAdmin(admin.ModelAdmin):
    list_display = ("apellido","nombre","email")
    list_filter = ("apellido",)

admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(Prestamo)
admin.site.register(Lector, LectorAdmin)

