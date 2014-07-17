from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('demo.apps.home.views',
		url(r'^$','index_view', name='vista_principal'),
		url(r'^about/$','about_view', name='vista_about'),
		url(r'^reserva/page/(?P<pagina>.*)/$','reservas_view', name='vista_reserva'),
		url(r'^reservas/(?P<id_resv>.*)/$','singleReserva_view', name='vista_single_reserva'),
		url(r'^contacto/$','contacto_view', name='vista_contacto'),
		url(r'^login/$','login_view', name='vista_login'),
		url(r'^registro/$','register_view', name='vista_registro'),
		url(r'^logout/$','logout_view', name='vista_logout'),
)

