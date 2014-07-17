from django import forms
from django.contrib.admin import widgets
from django.contrib.auth.models import User
#from demo.apps.home.models import userProfile

class ContactForm(forms.Form):
	Email	= forms.EmailField(widget=forms.TextInput())
	Titulo	= forms.CharField(widget=forms.TextInput())
	Texto	= forms.CharField(widget=forms.Textarea())

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))

class definirFechaForm(forms.Form):
	fecha_llegada = forms.CharField(widget=forms.TextInput())
	fecha_salida = forms.CharField(widget=forms.TextInput())	

	def __init__(self, *args, **kwargs):
		super(definirFechaForm, self).__init__(*args, **kwargs)
		self.fields['fecha_llegada'].widget = widgets.AdminDateWidget()
		self.fields['fecha_salida'].widget = widgets.AdminDateWidget()

class RegisterForm(forms.Form):
	username = forms.CharField(label="Nombre de Usuario", widget=forms.TextInput())
	first_name   = forms.CharField(label="Nombre Personal", widget=forms.TextInput())
	last_name    = forms.CharField(label="Apellido Personal", widget=forms.TextInput())
	nombre 	 = forms.CharField(label="Segundo Apellido", widget=forms.TextInput())
	email 	 = forms.EmailField(label="Email",widget=forms.TextInput())
	photo 	 = forms.ImageField()
	telefono = forms.CharField(label="Telefono",widget=forms.TextInput())
	password_one = forms.CharField(label="Password",widget=forms.PasswordInput(render_value=False))
	password_two = forms.CharField(label="Confirmar Password", widget=forms.PasswordInput(render_value=False) )

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError	('Este usuario ya existe')

	def clean_email(self):
			email = self.cleaned_data['email']
			try:
				u = User.objects.get(email=email)
			except User.DoesNotExist:	
				return email
			raise forms.ValidationError('Este email ya existe')	

	def clean_password_two(self):
		password_one = self.cleaned_data['password_one']
		password_two = self.cleaned_data['password_two']
		if password_one == password_two:
			pass	
		else:
			raise forms.ValidationError('Password no coinciden')	