from django import forms
from activos.models import ActivoEquipoOficina, ActivoExtintor, ActivoVehiculo

class ActivoExtintorForm(forms.ModelForm):
    class Meta:
        model=ActivoExtintor
        exclude=["estadoExtintor"]

class ActivoExtintorEditarForm(forms.ModelForm):
    class Meta:
        model=ActivoExtintor
        exclude=["estadoExtintor", "fechaIngresoExtintor"]

class ActivoEquipoOficinaForm(forms.ModelForm):
    class Meta:
        model=ActivoEquipoOficina
        exclude=["estadoEquipo"]

class ActivoEquipoOficinaEditarForm(forms.ModelForm):
    class Meta:
        model=ActivoEquipoOficina
        exclude=["estadoEquipo", "fechaIngresoEquipo"]

class ActivoVehiculoForm(forms.ModelForm):
    class Meta:
        model=ActivoVehiculo
        exclude=["estadoVehiculo"]

class ActivoVehiculoEditarForm(forms.ModelForm):
    class Meta:
        model=ActivoVehiculo
        exclude=["condicionVehiculo", "estadoVehiculo", "fechaIngresoVehiculo"]

