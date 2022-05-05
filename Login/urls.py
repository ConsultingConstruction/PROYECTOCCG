from django.urls import path,include

from .views import home,registrarUsuario,MenuUsuario

urlpatterns = [
    path('', home,name='index'),
    path('registrar/',registrarUsuario,name="registrarEmp"),
    path('menu/',MenuUsuario, name="menu"),
    
    #url de acceso
    
]