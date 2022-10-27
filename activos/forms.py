from django import forms
from activos.models import ActivoEquipoOficina, ActivoExtintor, ActivoVehiculo

class ActivoExtintorForm(forms.ModelForm):
    class Meta:
        model=ActivoExtintor
        exclude=["estadoExtintor"]

class ActivoEquipoOficinaForm(forms.ModelForm):
    class Meta:
        model=ActivoEquipoOficina
        exclude=["estadoEquipo"]

class ActivoVehiculoForm(forms.ModelForm):
    class Meta:
        model=ActivoVehiculo
        exclude=["estadoVehiculo"]

