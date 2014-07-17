from django import forms
from django.contrib.admin import widgets
from demo.apps.reserva.models import producto, cliente
from django.forms import ModelForm
from django.contrib import admin


class addReservaForm(forms.ModelForm):
	class Meta:
		model 	= producto
		exclude = {'status',}

	def __init__(self, *args, **kwargs):
		super(addReservaForm, self).__init__(*args, **kwargs)
		self.fields['fecha_inicio'].widget = widgets.AdminDateWidget()
		self.fields['fecha_final'].widget = widgets.AdminDateWidget()

class fechaForm(forms.ModelForm):
	class Meta:
		model 	= cliente
		exclude = {'status','nombre','apellido','mail','Telefono'}

	def __init__(self, *args, **kwargs):
		super(fechaForm, self).__init__(*args, **kwargs)
		self.fields['fecha_llegada'].widget = widgets.AdminDateWidget()
		self.fields['fecha_salida'].widget = widgets.AdminDateWidget()
		





"""class addReservaForm(forms.Form):
	nombre	 	= forms.CharField(widget=forms.TextInput())
	descripcion = forms.CharField(widget=forms.TextInput())
	direccion 	= forms.CharField(widget=forms.TextInput)
	imagen 		= forms.ImageField(required=False)
	precio 		= forms.DecimalField(required=True)
	sector		= forms.CharField(widget=forms.TextInput())
	fecha_inicio= forms.CharField(widget=forms.TextInput())

	""class Meta:
		model = addReserva

	def __init__(self,*args,**kwargs):
		super(addReservaForm, self).__init__(*args, **kwargs)
		self.fields['fecha_inicio'].widget = widgets.AdminSplitDateTime()
	""	

	def clean(self):
		return self.cleaned_data
"""