from django.shortcuts import render, redirect
from django.http import HttpResponse
from gestion_equipos.models import Equipo, Jugador
from gestion_equipos.forms import EquipoForm, JugadorForm, JugadorEnEquipoForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.views.generic import ListView, View, DetailView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
# Create your views here.

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

def avg(list):
	total=0.0
	if len(list) > 0:
		for l in list: total = total + l.edad
		return total/len(list)
	else:
		return 0

def index(request):
	return HttpResponse("Hello, world. You 're at the gestion_equipos index")

def detail(request, question_id):
	return HttpResponse("You 're looking at question %s." %question_id)

def index(request):
	listaEquipos = Equipo.objects.all()
	nombre = listaEquipos[0].nombre
	ciudad = listaEquipos[0].ciudad
	return HttpResponse ("Equipo: %s, Ciudad: %s" % (nombre,ciudad))

@login_required(login_url='/gestion_equipos/login')
def listaEquipos(request):
	listaEquipos = Equipo.objects.all().order_by("fundacion")
	context = { 'listaEquipos' : listaEquipos}
	return render(request, 'gestion_equipos/listaEquipos.html', context)


# @login_required(login_url='/gestion_equipos/login')
# def listaJugadores(request):
# 	listaJugadores = Jugador.objects.all().order_by("nombre")
# 	context = { 'listaJugadores' : listaJugadores}
# 	return render(request, 'gestion_equipos/listaJugadores.html', context)

class JugadoresListView(ListView):
	model = Jugador
	context_object_name = 'listaJugadores'
	template_name = 'gestion_equipos/listaJugadores.html'

@login_required(login_url='/gestion_equipos/login')
def equipo(request, equipo_id):
	equipo = Equipo.objects.get(pk=equipo_id)
	jugadores = Jugador.objects.filter(equipo=equipo)
	jugadores=jugadores.order_by("nombre")
	media = avg(jugadores)
	context = {'equipo' : equipo, 'jugadores' : jugadores, 'media' : media}
	return render(request, 'gestion_equipos/equipo.html', context)

@login_required(login_url='/gestion_equipos/login')
def jugador(request, jugador_id):
	jugador = Jugador.objects.get(pk=jugador_id)
	context = {'jugador' : jugador}
	return render(request, 'gestion_equipos/jugador.html', context)

@user_passes_test(lambda u: u.is_superuser,login_url='/gestion_equipos/login')
def nuevoEquipo(request):
	if request.method == 'POST':
		form = EquipoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/gestion_equipos/listaEquipos')
	else:
		form = EquipoForm()
	context = {'form':form}
	return render(request, 'gestion_equipos/nuevoEquipo.html', context)



# @user_passes_test(lambda u: u.is_superuser,login_url='/gestion_equipos/login')
# def nuevoJugador(request):
# 	if request.method == 'POST':
# 		form = JugadorForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('/gestion_equipos/listaJugadores')
# 	else:
# 		form = JugadorForm()
# 	context = {'form':form}
# 	return render(request, 'gestion_equipos/nuevoJugador.html', context)

class NuevoJugadorView(CreateView):
	model = Jugador
	fields = '__all__'
	template_name = 'gestion_equipos/nuevoJugador.html'

#@user_passes_test(lambda u: u.is_superuser,login_url='/gestion_equipos/login')
def nuevoJugadorEnEquipo(request, equipo_id):
	if request.method == 'POST':
		form = JugadorEnEquipoForm(request.POST, request.FILES)
		if form.is_valid():
			jugador=form.save(commit=False)
			jugador.equipo=Equipo.objects.get(id=equipo_id)
			jugador.save()
			context = {'jugador' : jugador}
			return render(request, 'gestion_equipos/jugador.html', context)
	else:
		form = JugadorEnEquipoForm()
	context = {'form':form}
	return render(request, 'gestion_equipos/nuevoJugadorEnEquipo.html', context)

#@user_passes_test(lambda u: u.is_superuser,login_url='/gestion_equipos/login')
def bajaJugador(request, jugador_id):
	jugador = Jugador.objects.get(pk=jugador_id)
	equipo=jugador.equipo.pk
	jugador.equipo = None
	jugador.save()
	context = {'jugador' : jugador}
	return render(request, 'gestion_equipos/jugador.html', context)

# #@user_passes_test(lambda u: u.is_superuser,login_url='/gestion_equipos/login')
# def eliminarJugador(request, jugador_id):
# 	jugador = Jugador.objects.get(pk=jugador_id)
# 	jugador.delete()
# 	return redirect('/gestion_equipos/listaJugadores')

class EliminarJugadorView(DeleteView):
	model = Jugador
	success_url = reverse_lazy('listaJugadores')

#@user_passes_test(lambda u: u.is_superuser,login_url='/gestion_equipos/login')
def eliminarEquipo(request, equipo_id):
	equipo = Equipo.objects.get(pk=equipo_id)
	equipo.delete()
	return redirect('/gestion_equipos/listaEquipos')

#@user_passes_test(lambda u: u.is_superuser,login_url='/gestion_equipos/login')
def modificarJugador(request, jugador_id):
	jugador = Jugador.objects.get(pk=jugador_id)
	if request.method == 'POST':
		form = JugadorForm(request.POST, request.FILES, instance=jugador)
		if form.is_valid():
			form.save()
			jugador=Jugador.objects.get(pk=jugador_id)
			context = {'jugador' : jugador}
			return render(request, 'gestion_equipos/jugador.html', context)
	else:
		form = JugadorForm(instance=jugador)
	context = {'form':form}
	return render(request, 'gestion_equipos/modificarJugador.html', context)

#@user_passes_test(lambda u: u.is_superuser,login_url='/gestion_equipos/login')
def modificarEquipo(request, equipo_id):
	equipo = Equipo.objects.get(pk=equipo_id)
	if request.method == 'POST':
		form = EquipoForm(request.POST, request.FILES, instance=equipo)
		if form.is_valid():
			form.save()
			jugadores = Jugador.objects.filter(equipo=equipo)
			jugadores=jugadores.order_by("nombre")
			media = avg(jugadores)
			context = {'equipo' : equipo, 'jugadores' : jugadores, 'media' : media}
			return render(request, 'gestion_equipos/equipo.html', context)
	else:
		form = EquipoForm(instance=equipo)
	context = {'form':form}
	return render(request, 'gestion_equipos/modificarEquipo.html', context)

def userLogin(request):
	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		if form.is_valid:
			user = request.POST['username']
			passwd = request.POST['password']
			access = authenticate(username=user, password=passwd)
			if access is not None:
				if access.is_active:
					login(request, access)
					return redirect('/gestion_equipos')
				else:
					return render(request, 'gestion_equipos/inactive.html')
			else:
				return render(request, 'gestion_equipos/nouser.html')
	else:
		form = AuthenticationForm()
	context = {'form': form}
	return render(request,'gestion_equipos/login.html', context)

#@login_required(login_url='/gestion_equipos/login')
def userLogout(request):
    logout(request)
    # Redirect to a success page.
    return redirect('/')

def userRegister(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        data = request.POST.copy()
        if form.is_valid:
            new_user = form.save(data)
            return redirect('/gestion_equipos')
    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request, "gestion_equipos/register.html", context)

