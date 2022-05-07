from django.urls import path,include

from . import views 


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.home,name='index'),
    path('registrar/',views.registrarUsuario,name="registrarEmp"),
    path('menu/',views.MenuUsuario, name="menu"),
    path('registrarV/',views.registrarVisistante,name='registrarVis'),
    path('administrarU/',views.administrarUsuarios,name='adminUsers'),    #url de acceso   
]