from django.shortcuts import render
from entrega_3.models import Tarea, Persona, Pais
from entrega_3.forms import TareaForm, PersonaForm, BuscarPersonasForm, PaisForm
from django.views.generic import ListView


def crear_tarea(request):
    f = TareaForm(request.POST)
    context = {
        "form": f
    } 
    if f.is_valid():
        Tarea(nombre=f.data["nombre"]).save()
        context['form'] = TareaForm()

    context["tareas"] = Tarea.objects.all()
    context["total_tareas"] = len(Tarea.objects.all())
         
    return render(request, "entrega_3/tareas.html", context)


def mostrar_personas(request):
    
    personas = Persona.objects.all()
    total_personas = len(personas)
    context = {
        "personas": personas, 
        "total_personas":total_personas,
        "form": PersonaForm(),
    }
    return render(request, "entrega_3/personas.html", context)


def crear_persona(request):

    f = PersonaForm(request.POST)
    context = {
        "form": f
    } 
    if f.is_valid():
        Persona(nombre=f.data["nombre"], apellido=f.data["apellido"], fecha_de_nacimiento=f.data["fecha_de_nacimiento"]).save()
        context['form'] = PersonaForm()

    context["personas"] = Persona.objects.all()
    context["total_personas"] = len(Persona.objects.all())
         
    return render(request, "entrega_3/personas.html", context)



class BuscarPersonas(ListView):
    model = Persona
    context_object_name = "personas"

    def get_queryset(self):
        f = BuscarPersonasForm(self.request.GET)
        if f.is_valid():
           return Persona.objects.filter(nombre__icontains=f.data["criterio_nombre"]).all()
        return Persona.objects.none()


def asignar_pais(request):
    f = PaisForm(request.POST)
    context = {
        "form": f
    } 
    if f.is_valid():
        Pais(pais=f.data["pais"]).save()
        context['form'] = PaisForm()

    context["paises"] = Pais.objects.all()
    context["total_paises"] = len(Pais.objects.all())
         
    return render(request, "entrega_3/paises.html", context)

