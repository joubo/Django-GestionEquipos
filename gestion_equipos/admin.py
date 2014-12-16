from django.contrib import admin

# Register your models here.

from gestion_equipos.models import Jugador, Equipo

admin.site.register(Jugador)
admin.site.register(Equipo)