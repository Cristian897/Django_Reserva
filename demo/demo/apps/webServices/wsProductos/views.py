# Create your views here.
from django.http import HttpResponse
from demo.apps.reserva.models import producto
#integramos la serializacion
from django.core import serializers

def wsProductos_view(request):
	data = serializers.serialize("json",producto.objects.filter(status=True))
	#retorna informacion en formato json
	return HttpResponse(data,mimetype='application/json')
