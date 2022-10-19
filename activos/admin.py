from django.contrib import admin
from .models import ActivoExtintor,ActivoEquipoOficina,ActivoVehiculo
# Register your models here.

admin.site.register(ActivoExtintor)
admin.site.register(ActivoEquipoOficina)
admin.site.register(ActivoVehiculo)
