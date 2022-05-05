from django.urls import path,include
from .views import OMC23

urlpatterns = [
    path('', OMC23,name='omc23'),
    
]