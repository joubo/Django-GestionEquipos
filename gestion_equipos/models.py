from django.db import models

# Create your models here.

class Equipo(models.Model):

	nombre = models.CharField(max_length = 100, unique = True)
	ciudad = models.CharField(max_length = 100, default = "")
	fundacion = models.IntegerField()
	entrenador = models.CharField(max_length = 100, unique = True, default = "")
	historia = models.TextField(blank = True, default = "")

	def __unicode__(self):
		return self.nombre

class Jugador(models.Model):

	nombre = models.CharField(max_length = 100)
	fecha_nacimiento = models.DateField(default="1970-01-01")
	lugar_nacimiento = models.CharField(max_length = 100, default ="")
	edad = models.IntegerField()
	equipo = models.ForeignKey(Equipo, null = True, blank = True)
	posicion = models.CharField(max_length = 100, default = "")
	historial = models.TextField(blank = True, default = "")

	def __unicode__(self):
		return self.nombre

	def print_details(self):
		return "El Jugador %s %s pertenece al Equipo %s" % (self.nombre, self.apellidos, self.equipo)
