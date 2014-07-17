from django.contrib import admin
from demo.apps.reserva.models import cliente,producto,reserva


class reservaAdmin(admin.ModelAdmin):
	list_display = ('nombreCasa','nombreCliente','sector')
	list_filter = ('nombreCasa','nombreCliente','sector', 'precio')
	search_fields = ['sector']

#Registro modelos
admin.site.register(cliente)
admin.site.register(producto)
admin.site.register(reserva, reservaAdmin)
#admin.site.register(fijar_fecha)
