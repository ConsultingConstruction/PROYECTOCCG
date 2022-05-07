from django.shortcuts import render,redirect
from .forms import LoginForm,FormularioPersonal,FormulariUsuario,FormularioInvitado
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from .models import Usuario,Pais,Estado,Mundeleg,Cp,Personal
from django.contrib import messages
from django.forms import ValidationError


def inicio(request):
    return render(request,'inicio.html')


# def home(request):
#       message = None
#       if request.method == 'POST':
#          form = LoginForm(request.POST)
#          print(form.errors)
#          if form.is_valid():
#             message = "holaaa"
#             username = request.POST['username']
#             password =  request.POST['password']
#             user = Usuario.objects.get(username)
#             passw = Usuario.objects.get(password)
#             user = authenticate(username=user,password=passw)
#             if user is not None:
#                if user.is_active:
#                   login(request,user)
#                   message = "Te haz identificado de modo correcto"
#                else:
#                   message = "Tu usuario esta inactivo"
#             else:
#                message = "Nombre de usuario o contraseña incorrecta"
#       else:
#          form = LoginForm()
      
#       return render(request,'registration/login.html',{'form':form,'message':message},)
     
def home(request):
      if request.method == 'POST':
         try:
            datosUsuario = Usuario.objects.get(username=request.POST['username'],password=request.POST['password'])
            print('Usuario = ',datosUsuario)
            request.session['username']=datosUsuario.username
            return render(request,'menu.html')
         except Usuario.DoesNotExist as e:
               messages.success(request,'nombre o contraseña incorecta')
      return render(request,'registration/login.html',{},)



@login_required
def MenuUsuario(request):
      return render(request,'menu.html')

      
def registrarUsuario(request):
        pais = Pais.objects.all()
        estado = Estado.objects.all()
        municipio = Mundeleg.objects.all()
        cp = Cp.objects.all()
        message = None
        

        if request.method == 'POST':
             formU = FormulariUsuario(request.POST)
             formP = FormularioPersonal(request.POST)
             print(formP.errors)
             if formU.is_valid() and formP.is_valid():
                new_formP = formP.save(commit=False)
                new_formU = formU.save(commit = False)
                new_formU.rol = 'Empleado'
                value_cp = request.POST.get('cp')
                new_formP.fk_cp = value_cp
                new_formU.save()
                print(formP.errors)
                new_formP.fk_usuario = new_formU.idusuario
                print(formP.errors)
                new_formP.save()

        else:
              formU = FormulariUsuario()
              formP = FormularioPersonal()
        return render(request,'RegistroEmpleado.html',{'pais':pais,'estado':estado,'municipio':municipio, 'cp': cp,'formU':formU,'formP':formP},)

def registrarVisistante(request):

        
        pais = Pais.objects.all()
        estado = Estado.objects.all()
        municipio = Mundeleg.objects.all()
        cp = Cp.objects.all()
        messages
        if request.method == 'POST':
          formV = FormularioInvitado(request.POST)
          formU = FormulariUsuario(request.POST)
          print(formV.errors)
          if formV.is_valid() and formU.is_valid():
             new_formV = formV.save(commit=False)
             new_formU = formU.save(commit=False)
             new_formU.rol = 'Visitante'
             value_mun = request.POST.get('mundeleg')
             new_formV.fk_mundeleg = value_mun
             new_formU.save()
             new_formV.fk_usuario = new_formU.idusuario
             print(formV.errors)
             new_formV.save()
             
             messages.success(request, 'Your password was updated successfully!') 
             return redirect('registrarVis')
          else:
             messages.warning(request, 'Please correct the error below.')
             
        else:
             formU = FormulariUsuario()
             formV = FormularioInvitado()

              
        return render(request,'RegistroVisitante.html',{'pais':pais,'estado':estado,'municipio':municipio, 'cp': cp,'formU':formU,'formV':formV},)



def administrarUsuarios(request):
      usuarios = Usuario.objects.all()
      
      contexto={
         'usuarios':usuarios,
      }
      
      return render(request,'AdministrarUsuarios.html',contexto)