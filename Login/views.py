from django.shortcuts import render
from .forms import LoginForm

# Create your views here.

def home(request):
      form = LoginForm()

      return render(request,'registration/login.html',{'form':form})

def registrarUsuario(request):
      return render (request,'RegistroEmpleado.html')


def MenuUsuario(request):
      return render (request,'menu.html')