from django.conf.urls import patterns, url
from gestion_equipos import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth.views import login, logout
from gestion_equipos.views import JugadoresListView, NuevoJugadorView, EliminarJugadorView
#Hacer las direcciones entendibles

#http://127.0.0.1:8000/-------de aqui hacia adelante------app/lista
#Lo normal es hacer http://127.0.0.1:8000/equipos/ una direccion base

urlpatterns = patterns('',
	url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
	url(r'^$', TemplateView.as_view(template_name='gestion_equipos/index.html'),name='index'),
	url(r'^listaEquipos/$', views.listaEquipos, name = "listaEquipos"),
	url(r'^listaJugadores/$', JugadoresListView.as_view(), name = "listaJugadores"),
	url(r'^nuevoEquipo/$', views.nuevoEquipo, name = "nuevoEquipo"),
	url(r'^nuevoJugador/$', NuevoJugadorView.as_view(success_url='/gestion_equipos/listaJugadores'), name = "nuevoJugador"),
	url(r'^equipo/nuevoJugadorEnEquipo/(?P<equipo_id>\d+)/$', views.nuevoJugadorEnEquipo, name = "nuevoJugadorEnEquipo"),
	url(r'^equipo/(?P<equipo_id>\d+)/$', views.equipo, name = "equipo"),
	url(r'^jugador/(?P<jugador_id>\d+)/$', views.jugador, name = "jugador"),
	url(r'^bajaJugador/(?P<jugador_id>\d+)/$',views.bajaJugador, name = "bajaJugador"),
	url(r'^eliminarJugador/(?P<pk>\d+)/$',EliminarJugadorView.as_view(success_url='/gestion_equipos/listaJugadores'), name = "eliminarJugador"),
	url(r'^eliminarEquipo/(?P<equipo_id>\d+)/$',views.eliminarEquipo, name = "eliminarEquipo"),
	url(r'^modificarJugador/(?P<jugador_id>\d+)/$',views.modificarJugador, name = "modificarJugador"),
	url(r'^modificarEquipo/(?P<equipo_id>\d+)/$',views.modificarEquipo, name = "modificarEquipo"),
	url(r'^login/$', views.userLogin, name = "login"),
    url(r'^logout/$', views.userLogout, name = "logout"),
    url(r'^register/$',views.userRegister, name="register"),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	