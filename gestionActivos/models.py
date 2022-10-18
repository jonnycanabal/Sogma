from django.utils.translation import gettext_lazy as _
from django.db import models

from activos.models import ActivoEquipoOficina, ActivoExtintor, ActivoVehiculo, Pasajero
from usuarios.models import Usuario

# Create your models here.

# CREACIÓN DE LA TABLA (generarAlarma) DE NUESTRA MER DISEÑADO EN MYSQL WORKBENCH
class GenerarAlarma(models.Model):
    # REVISAR ESTAR PARTE SI ESTA BIEN DECLARADA O LLAMADA LA FOREING KEY
    fkIdExtintor=models.ForeignKey(ActivoExtintor, on_delete=models.CASCADE, verbose_name="Extintor")
    fkIdEquipoOficina=models.ForeignKey(ActivoEquipoOficina, on_delete=models.CASCADE, verbose_name="Equipo de Oficina")
    fkVehiculo=models.ForeignKey(ActivoVehiculo, on_delete=models.CASCADE, verbose_name="Vehículo")
    fechaMantenimiento=models.DateField(verbose_name="Fecha Mantenimiento", help_text="MM/DD/AAAA")
    class TipoMantenimiento(models.TextChoices):
        PERIODICO='Periodico', _("Periodico")
        PREVENTIVO='Preventivo', _("Preventivo")
        KILOMETRAJE='Kilometraje', _("Kilometraje")
    tipoMantenimiento=models.CharField(max_length=15, choices=TipoMantenimiento.choices, default=TipoMantenimiento.PREVENTIVO, verbose_name="Tipo de Mantenimiento")
    descripcionMantenimiento=models.TextField(max_length=100, verbose_name="Descripción del Mantenimiento")

# CREACIÓN DE LA TABLA (generarRuta) DE NUESTRA MER DISEÑADO EN MYSQL WORKBENCH
class GenerarRuta(models.Model):
    # FOREING KEY REREFENCIADA DEL MODELO ACTIVOS DE LAS CLASES REQUERIDAS VEHICULO, USUARIO Y PASAJERO.
    fkVehiculo=models.ForeignKey(ActivoVehiculo, on_delete=models.CASCADE, verbose_name="Vehículo")
    fkUsuario=models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario")
    fkPasajero=models.ForeignKey(Pasajero, on_delete=models.CASCADE, verbose_name="Pasajero")
    horaSalida=models.TimeField(verbose_name="Hora de Salida", help_text="HH:MM")
    horaRegreso=models.TimeField(verbose_name="Hora de Regreso", help_text="HH:MM")
    fechaSalida=models.DateField(verbose_name="Fecha de Salida", help_text="MM/DD/AAAA")
    fechaRegreso=models.DateField(verbose_name="Fecha de Regreso", help_text="MM/DD/AAAA")
    lugarSalida=models.CharField(max_length=50, verbose_name="Lugar de Salida")
    lugarDestino=models.CharField(max_length=50, verbose_name="Lugar de Destino")
    kilometrajeFinalVehiculo=models.IntegerField(verbose_name="Kilometraje Final")  # Valor numero (IntegerField) Para sumar Kilometraje!!!!!!
    descripcionRuta=models.TextField(max_length=100, verbose_name="Descripción")
    observacionesRuta=models.TextField(max_length=100, verbose_name="Observaciones")

# CREACIÓN DE LA TABLA (registrarMantenimiento) DE NUESTRA MER DISEÑADO EN MYSQL WORKBENCH
class RegistrarMantenimiento(models.Model):
    # FOREING KEY REREFENCIADA DEL MODELO ACTIVOS DE LAS CLASES REQUERIDAS EXTINTOR, EQUIPO OFICINA, VEHICULO.
    fkIdExtintor=models.ForeignKey(ActivoExtintor, on_delete=models.CASCADE, verbose_name="Extintor")
    fkIdEquipoOficina=models.ForeignKey(ActivoEquipoOficina, on_delete=models.CASCADE, verbose_name="Equipo de Oficina")
    fkVehiculo=models.ForeignKey(ActivoVehiculo, on_delete=models.CASCADE, verbose_name="Vehículo")
    fechaMantenimiento=models.DateField(verbose_name="Fecha del Mantenimiento", help_text="MM/DD/AAAA")
    lugarMantenimiento=models.CharField(max_length=50, verbose_name="Lugar del Mantenimiento")
    ciudadMantenimiento=models.CharField(max_length=20, verbose_name="Lugar del Mantenimiento")
    kilometrajeMantenimiento=models.IntegerField(verbose_name="Kilometraje del Vehículo") # Valor numero (IntegerField) Para sumar Kilometraje!!!!!!
    numeroFactura=models.CharField(max_length=10, verbose_name="Número de Factura")
    valorMantenimiento=models.IntegerField(verbose_name="Valor del Mantenimiento") # Valor numero (IntegerField)!!!!!!
    descripcionMantenimiento=models.TextField(max_length=200, verbose_name="Descripción")
    
    # (!!!!!!!!!ADJUNTAR ARCHIVO DEL MANTENIMIENTO - PENDIENTE POR ESTABLECER SI ES LA FORMA ADECUADA!!!!!!!!)
    # adjuntarArchivoMantenimiento=models.FileField(upload_to='uploads', blank=True)
    # adjuntarArchivoMantenimiento=models.ImageField(upload_to='uploads', blank=True)



