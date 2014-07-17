from django.db import models

# Create your models here.
class cliente(models.Model):

	nombre 		= models.CharField(max_length=200)
	apellido 	= models.CharField(max_length=200)
	mail		= models.CharField(max_length=200)
	Telefono	= models.CharField(max_length=200)
	status		= models.BooleanField(default=True)	
	#fechas de cliente a reservar
	fecha_llegada	= models.DateField()
	fecha_salida	= models.DateField()
	
	def __unicode__(self):
		nombreCompleto = "%s %s"%(self.nombre,self.apellido)
		return nombreCompleto
	
class producto(models.Model):

	def url(self,filename):
		ruta = "MultimediaData/Reserva/%s/%s"%(self.nombre,str(filename))
		return ruta

	nombre 		= models.CharField(max_length=200)
	descripcion = models.TextField(max_length=300)
	direccion	= models.CharField(max_length=200)
	precio		= models.DecimalField(max_digits=6,decimal_places=2)
	sector		= models.CharField(max_length=200)
	status		= models.BooleanField(default=True)	
	imagen 		= models.ImageField(upload_to=url,null=True,blank=True)
	fecha_inicio	= models.DateField()
	fecha_final 	= models.DateField()
	
	def __unicode__(self):
		return self.nombre

class reserva(models.Model):

	def url(self,filename):
		ruta = "MultimediaData/ReservadoCasa/%s/%s"%(self.nombreCasa,str(filename))
		return ruta

	nombreCasa 	= models.CharField(max_length=200)
	nombreCliente = models.CharField(max_length=200)
	descripcion = models.TextField(max_length=300)
	direccion	= models.CharField(max_length=200)
	imagen 		= models.ImageField(upload_to=url,null=True,blank=True)
	precio		= models.DecimalField(max_digits=6,decimal_places=2)
	sector		= models.CharField(max_length=200)
	fecha_llegada= models.DateField()
	fecha_salida = models.DateField()
	status	= models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombreCasa

"""class fijar_fecha(models.Model):

	nombre_casa		= models.CharField(max_length=200)
	fecha_llegada	= models.DateField()
	fecha_salida	= models.DateField()	

	def __unicode__(self):
		dato = "%s %s"%(self.nombre_casa,self.fecha_llegada)
		return dato
"""
