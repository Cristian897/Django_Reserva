# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.apps.reserva.forms import addReservaForm
from demo.apps.reserva.models import producto, reserva, cliente
from django.http import HttpResponseRedirect
from datetime import date

def add_reserva_view(request):
	info = "iniciado"
	if request.method =="POST":
		form = addReservaForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.status = True
			add.save()#Guardar informacion
			info = "Guardado satisfactoriamente"
			return HttpResponseRedirect('/reservas/%s'%add.id)
	else:	
		form = addReservaForm()
	ctx = {'form':form,'informacion':info}	
	return render_to_response('reserva/addReserva.html',ctx, context_instance=RequestContext(request))





def edit_reserva_view(request, id_resv):
	info = "iniciado"
	resv = producto.objects.get(id=id_resv)
	if request.method == "POST":
		form = addReservaForm(request.POST,request.FILES,instance=resv)
		if form.is_valid():
			edit = form.save(commit=False)
			edit.status = True
			edit.save()#Guardar edicion de formulario
			info = "Correcto"
			return HttpResponseRedirect('/reservas/%s'%edit.id)
	else:	
		form = addReservaForm(instance=resv)
	ctx = {'form':form,'informacion':info}	
	return render_to_response('reserva/editReserva.html',ctx, context_instance=RequestContext(request))


def reserva_casa_view(request,id_resv):	
	if request.user.is_authenticated():
		resv = producto.objects.get(id=id_resv)
		cli = request.user
		print cli,resv
		c = cliente()
		rc = reserva()
		rc.nombreCasa = resv.nombre
		rc.nombreCliente = cli
		rc.descripcion = resv.descripcion
		rc.direccion = resv.direccion
		rc.imagen = resv.imagen
		rc.precio = resv.precio
		rc.sector = resv.sector
		rc.fecha_llegada = rc.fecha_llegada #resv.fecha_inicio#rc.fecha_llegada #fecha del cliente
		rc.fecha_salida = rc.fecha_salida #resv.fecha_final#rc.fecha_salida ##fecha del cliente
		rc.save()
		resv.status = False
		resv.save()


		#r = reserva()
		#f.nombreCliente = cli
		return HttpResponseRedirect('/')

"""
def edit_reserva_view(request, id_resv):
	r = producto.objects.get(id=id_resv)
	if request.method=='POST':
		form = addReservaForm(request.POST,request.FILES)
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			descripcion = form.cleaned_data['descripcion']
			imagen = form.cleaned_data['imagen']
			precio = form.cleaned_data['precio']
			sector = form.cleaned_data['sector']
			direccion = form.cleaned_data['direccion']
			fecha_inicio = form.cleaned_data['fecha_inicio']
			fecha_final = form.cleaned_data['fecha_final']
			r.nombre = nombre
			r.descripcion = descripcion
			r.direccion = direccion
			r.precio = precio
			r.sector = sector
			r.status = True
			r.fecha_inicio = fecha_inicio
			r.fecha_final = fecha_final
			if imagen:
					r.imagen = imagen
			r.save()	
	if request.method == 'GET':
		form = addReservaForm(initial={
								r.nombre = nombre
								r.descripcion = descripcion
								r.direccion = direccion
								r.precio = precio
								r.sector = sector
								r.status = True
								r.fecha_inicio = fecha_inicio
								r.fecha_final = fecha_final

			})
	ctx = {'form':form, 'producto':producto}	
	return render_to_response('reserva/editReserva.html',ctx, context_instance=RequestContext(request))
"""	

"""
def add_reserva_view(request):
	if request.user.is_authenticated():

		if request.method == "POST":
			form = addReservaForm(request.POST,request.FILES)
			info = "Inicializando"
			if form.is_valid():
					nombre = form.cleaned_data['nombre']
					descripcion = form.cleaned_data['descripcion']
					direccion = form.cleaned_data['direccion']
					precio = form.cleaned_data['precio']
					sector = form.cleaned_data['sector']
					imagen = form.cleaned_data['imagen']
					fecha_inicio = form.cleaned_data['fecha_inicio']

					r = producto()
					if imagen:#validacion
						r.imagen = imagen
					r.nombre = nombre
					r.descripcion = descripcion
					r.direccion = direccion
					r.precio = precio
					r.sector = sector
					r.status = True
					r.fecha_inicio = fecha_inicio
					r.save() # gurdar la info 
					info = "Se guardo satisfactoriamente"
			else:
				info = "Informacion con datos incorrectos"
			form = addReservaForm()
			ctx = {'form':form, 'informacion':info}	
			return render_to_response('reserva/addReserva.html',ctx, context_instance=RequestContext(request))
		else:#get
			form = addReservaForm()
			ctx = {'form':form}
			return render_to_response('reserva/addReserva.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')

"""