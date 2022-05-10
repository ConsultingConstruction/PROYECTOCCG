from django.urls import path,include

from . import views 


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.loginEntrar,name='index'),
    path('logout/',views.logoutSalir, name="logout"),
    path('registrar/',views.registrarUsuario,name="registrarEmp"),
    path('menu/',views.MenuUsuario, name="menu"),
    path('registrarV/',views.registrarVisistante,name='registrarVis'),
    path('administrarU/',views.administrarUsuarios,name='adminUsers'),
    path('Modificar/<int:id>/', views.EditarUser, name ='modificar'), 
    path('Eliminar/<int:id>/',views.EliminarUsuario,name ='eliminar')  #url de acceso   
]