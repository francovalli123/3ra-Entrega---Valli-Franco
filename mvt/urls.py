"""mvt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from entrega_3.views import  crear_tarea, mostrar_personas, crear_persona, BuscarPersonas, asignar_pais

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('tareas', crear_tarea, name="tareas"),
    path('personas', mostrar_personas, name="personas"),
    path('personas/create', crear_persona, name="personas-create"),
    path('personas/list', BuscarPersonas.as_view(), name="personas-list"),
    path('paises', asignar_pais, name="paises"),
]
