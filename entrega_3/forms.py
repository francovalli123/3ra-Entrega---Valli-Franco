from django import forms

class TareaForm(forms.Form):
    nombre = forms.CharField(max_length=100)

class PersonaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    fecha_de_nacimiento = forms.DateField()


class BuscarPersonasForm(forms.Form):
    criterio_nombre = forms.CharField(max_length=100)

class PaisForm(forms.Form):
    pais = forms.CharField(max_length=100)



