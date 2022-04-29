from django.forms import ModelForm
from .models import Usuario
from django import forms

CHOICES=[('H','Hombre'),
         ('M','Mujer')]


class LoginForm(ModelForm):
      class Meta:
       model = Usuario
       fields =   ('username','password',)

       widgets = {
           'username': forms.TextInput(attrs={'placeholder':'example@prueba.com', 'id':'username', 'name':'idusername', 'class':'item-mail'}),
           'password': forms.PasswordInput(attrs={'placeholder': 'Contraseña...', 'class':'item-password'})
       }

       labels = {
           'correo':'Correo',
           'password': 'Contraseña'
       }
    


# class FormularioPersonal(ModelForm):
#     class Meta:
#      model = Personal
#      fields = ('nombre','paterno','materno','genero','fechanac','lugarnac','rfc','curp','cel','calle','noint','noext')
     
#      widgets = {
#         'fechanac' : forms.DateInput(attrs={'type': 'date'}),
#         'genero' : forms.RadioSelect(choices = CHOICES, attrs={'class':'Boton-radio'})
#     }

