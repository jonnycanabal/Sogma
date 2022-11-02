from django.contrib import admin
from .models import GenerarRuta, Pasajero, RegistrarMantenimiento, MantenimientoVehiculo, MantenimientoExtintor, MantenimientoEquipo

# Register your models here.

admin.site.register(GenerarRuta)
admin.site.register(Pasajero)
admin.site.register(RegistrarMantenimiento)
admin.site.register(MantenimientoVehiculo)
admin.site.register(MantenimientoExtintor)
admin.site.register(MantenimientoEquipo)

