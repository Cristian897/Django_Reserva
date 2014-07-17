# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.apps.reserva.models import producto, reserva, cliente
from demo.apps.home.forms import ContactForm, LoginForm, definirFechaForm, RegisterForm
from demo.apps.reserva.forms import addReservaForm, fechaForm
from django.core.mail import EmailMultiAlternatives #Envia HTML
from django.contrib.auth.models import User
from demo.apps.home.models import userProfile

from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator,EmptyPage, InvalidPage
from django.core.mail import send_mail

def index_view(request):
	return render_to_response('home/index.html', context_instance=RequestContext(request))

def about_view(request):
	mensaje = "mensaje desde mi vista"
	ctx = {'msg' :mensaje}
	return render_to_response('home/about.html', ctx, context_instance=RequestContext(request))

def reservas_view(request,pagina):
	lista_prod = producto.objects.filter(status=True)#select * from reserva_productos where status = true
	paginator = Paginator(lista_prod,5)#productos or pagina
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		productos = paginator.page(page)	
	except(EmptyPage,InvalidPage):
		productos = paginator.page(paginator.num_pages)
	#lista_resv = reserva.objects.filter(status=True)
	ctx = {'productos':productos}
	return render_to_response('home/reserva.html', ctx, context_instance=RequestContext(request))

def contacto_view(request):
	info_enviado = False #definir si se envia la info o no
	email	= ""
	titulo	= ""
	texto 	= ""
	if request.method == "POST":
		formulario = ContactForm(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['Email']
			titulo = formulario.cleaned_data['Titulo']
			texto = formulario.cleaned_data['Texto']

			#Configuracion de envio de mail (Gmail)
			to_admin = 'scristian9216@gmail.com'
			html_content = "Informacion recibida de [%s]<br><br>***Mensaje***<br>%s"%(email,texto)
			msg = EmailMultiAlternatives('Correo de Contacto',html_content,'from@server.com',[to_admin])
			msg.attach_alternative(html_content,'text/html')#Definios el contenido como html
			msg.send()#Envio de correo
	else:	
		formulario = ContactForm()#formlacio vacio
	ctx 	= {'form':formulario, 'email':email, 'titulo':titulo, 'texto':texto, 'info_enviado':info_enviado}
	return render_to_response('home/contacto.html',ctx, context_instance=RequestContext(request))


def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if  request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				usuario = authenticate(username=username, password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect('/')
				else:
					mensaje="usuario o password incorrecto"	
		form = LoginForm()
		ctx = {'form':form,'mensaje':mensaje}
		return render_to_response('home/login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')	

def singleReserva_view(request,id_resv):
	info = "inicio"
	cli = request.user
	resv = producto.objects.get(id=id_resv)
	r = reserva()
	if request.method == "POST":
		form = definirFechaForm(request.POST)
		if form.is_valid():
			r.nombreCasa = resv.nombre
			r.nombreCliente = cli
			r.descripcion = resv.descripcion
			r.direccion = resv.direccion
			r.sector = resv.sector
			r.imagen = resv.imagen
			r.precio = resv.precio
			#r.status = True
			r.fecha_llegada = form.cleaned_data['fecha_llegada']
			r.fecha_salida  = form.cleaned_data['fecha_salida']

			#rc.fecha_llegada = fecha_inicio
			#resv.fecha_final  = fecha_final
			r.save()
			resv.status = True
			resv.save()
			info = "Se guardo satisfactoriamente"
			return HttpResponseRedirect('/')
		else:
			info = "datos incorrectos"
		form = definirFechaForm()
		ctx = {'producto':resv,'form':form, 'informacion':info}	
		return render_to_response('home/SingleReserva.html',ctx,context_instance=RequestContext(request))
	else:#get	
		form = definirFechaForm()		
		ctx = {'producto':resv,'info':info,'form':form}
		return render_to_response('home/SingleReserva.html',ctx,context_instance=RequestContext(request))



"""
def singleReserva_view(request,id_resv):
	info="iniciado"
	resv = producto.objects.get(id=id_resv)
	if request.method =="POST":
		form = fechaForm(request.POST, request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.status = True
			add.nombre = resv.nombre
			add.apellido = ""
			add.mail = ""
			add.telefono = ""
			add.save()
			return HttpResponseRedirect('/reservas/%s'%add.id)
	else:
		form = fechaForm(instance=resv)
	ctx = {'producto':resv, 'form':form, 'informacion':info}
	return render_to_response('home/SingleReserva.html',ctx,context_instance=RequestContext(request))
	
"""

def register_view(request):
	form = RegisterForm()
	if request.method =="POST":
		form = RegisterForm(request.POST,request.FILES)
		if form.is_valid():
			usuario = form.cleaned_data['username']
			first_name  = form.cleaned_data['first_name']
			last_name	= form.cleaned_data['last_name']
			email = form.cleaned_data['email']
			password_one = form.cleaned_data['password_one']
			password_two = form.cleaned_data['password_two']
			u = User.objects.create_user(username=usuario, email=email, password=password_one, first_name=first_name, last_name=last_name)
			u.save()#Guardar el objeto usuario
			#Completando perfil de usuario
			perfil = userProfile()
			perfil.user = u
			perfil.nombre = form.cleaned_data['nombre']
			perfil.photo = form.cleaned_data['photo']
			perfil.telefono = form.cleaned_data['telefono']
			#perfil.photo = photo
			perfil.save()#Guardar Datos del perfil

			return render_to_response('home/thanks_register.html', context_instance=RequestContext(request))
		else:
			ctx = {'form':form}
			return render_to_response ('home/register.html',ctx,context_instance=RequestContext(request))	
	ctx={'form':form}
	return render_to_response('home/register.html',ctx, context_instance=RequestContext(request))


