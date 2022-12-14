from dataclasses import field
from django import forms
from gestionActivos.models import Alarmas, GenerarRuta, Pasajero, RegistrarMantenimiento, DetalleRuta

class AlarmasForm(forms.ModelForm):
    class Meta:
        model=Alarmas
        fields='__all__'

class GenerarRutaForm(forms.ModelForm):
    class Meta:
        model=GenerarRuta
        exclude=['horaRegreso','kilometrajeFinalVehiculo','observacionesRuta', 'estadoRuta']

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
        exclude=['estadoPasajero']

