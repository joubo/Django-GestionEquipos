#encoding: utf-8
from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm
from django import forms
from gestion_equipos.models import Equipo, Jugador
from django.contrib.auth.models import User

class EquipoForm(ModelForm):
	class Meta:
		model=Equipo

		#exclude = ['pk', 'equipo']
		fields = '__all__'

class JugadorForm(ModelForm):
	class Meta:
		model=Jugador

		#exclude = ['pk']
		fields = '__all__'

class JugadorEnEquipoForm(ModelForm):
	class Meta:
		model=Jugador

		exclude = ['equipo']
		fields = '__all__'