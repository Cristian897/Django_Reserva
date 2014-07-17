from django.contrib import admin
from demo.apps.ventas.models import cliente,producto

#registramos modelos de ventas
admin.site.register(cliente)
admin.site.register(producto)