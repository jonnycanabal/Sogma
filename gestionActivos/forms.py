from dataclasses import field
from django import forms
from gestionActivos.models import GenerarAlarma, GenerarRuta, Pasajero, RegistrarMantenimiento, DetalleRuta

class GenerarAlarmaForm(forms.ModelForm):
    class Meta:
        model=GenerarAlarma
        fields='__all__'

class GenerarRutaForm(forms.ModelForm):
    class Meta:
        model=GenerarRuta
        exclude=['horaRegreso','kilometrajeFinalVehiculo','observacionesRuta']

class EditarGenerarRutaForm(forms.ModelForm):
    class Meta:
        model=GenerarRuta
        fields=['horaRegreso','kilometrajeFinalVehiculo','observacionesRuta']

class DetalleRutaForm(forms.ModelForm):
    class Meta:
        model=DetalleRuta
        fields='__all__'

class RegistrarMantenimientoForm(forms.ModelForm):
    class Meta:
        model=RegistrarMantenimiento
        fields='__all__'

class PasajeroForm(forms.ModelForm):
    class Meta:
        model=Pasajero
        fields='__all__'

