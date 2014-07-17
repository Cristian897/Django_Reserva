from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('demo.apps.reserva.views',
		url(r'^add/reserva/$','add_reserva_view', name='vista_agregar_reserva'),
		url(r'^edit/reserva/(?P<id_resv>.*)/$','edit_reserva_view', name='vista_editar_reserva'),
		url(r'^confirmar/reserva/(?P<id_resv>.*)/$','reserva_casa_view', name='vista_reserva_casa'),
				
)