from django.urls import path
from activos.views import control_activos, control_activos_eliminar_equipo, control_activos_eliminar_extintor, control_activos_eliminar_vehiculo

urlpatterns = [
    path('controlActivos/', control_activos,  name="control-activos"),
    path('controlActivos/eliminar/vehiculo/<int:pk>/', control_activos_eliminar_vehiculo, name="control-activos-eliminar-vehiculo"),
    path('controlActivos/eliminar/extintor/<int:pk>/', control_activos_eliminar_extintor, name="control-activos-eliminar-extintor"),
    path('controlActivos/eliminar/equipo/<int:pk>/', control_activos_eliminar_equipo, name="control-activos-eliminar-equipo"),
]