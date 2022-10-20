from django import forms
from activos.models import ActivoEquipoOficina, ActivoExtintor, ActivoVehiculo

class ActivoExtintorForm(forms.ModelForm):
    class Meta:
        model=ActivoExtintor
        fields='__all__'

class ActivoEquipoOficinaForm(forms.ModelForm):
    class Meta:
        model=ActivoEquipoOficina
        exclude=["estado"]

class ActivoVehiculoForm(forms.ModelForm):
    class Meta:
        model=ActivoVehiculo
        exclude=["estado"]

