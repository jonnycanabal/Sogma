from django import forms
from gestionActivos.models import GenerarAlarma, GenerarRuta, RegistrarMantenimiento

class GenerarAlarmaForm(forms.ModelForm):
    class Meta:
        model=GenerarAlarma
        fields='__all__'

class GenerarRutaForm(forms.ModelForm):
    class Meta:
        model=GenerarRuta
        fields='__all__'

class RegistrarMantenimientoForm(forms.ModelForm):
    class Meta:
        model=RegistrarMantenimiento
        fields='__all__'
