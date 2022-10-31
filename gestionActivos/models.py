from tabnanny import verbose
from django.utils.translation import gettext_lazy as _
from django.db import models

from activos.models import ActivoEquipoOficina, ActivoExtintor, ActivoVehiculo
from usuarios.models import Usuario

# Create your models here.

# ###############################################################################################################################
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


# ###############################################################################################################################
# CREACIÓN DE LA TABLA (pasajero) DE NUESTRA MER DISEÑADO EN MYSQL WORKBENCH
class Pasajero(models.Model):
    primerNombrePasajero=models.CharField(max_length=50, verbose_name="Primer Nombre")
    primerApellidoPasajero=models.CharField(max_length=50, verbose_name="Primer Apellido")
    class TipoDocumentoPasajero(models.TextChoices):
        CC='C.C.', _("Cédula de Ciudadania")
        CE='C.E.', _("Cédula de Extranjería")
        PASS='PASS', _("Pasaporte")
    tipoDocumento=models.CharField(max_length=5, choices=TipoDocumentoPasajero.choices, default=TipoDocumentoPasajero.CC, verbose_name="Tipo de Documento")
    numeroDocumentoPasajero=models.CharField(max_length=50, unique=True, verbose_name="Número de Documento") #Tiene campo Único
    direccionPasajero=models.CharField(max_length=100, verbose_name="Dirección Residencia")
    telefonoPasajero=models.CharField(max_length=20, verbose_name="Teléfono")
    def __str__(self):
        return "%s %s"%(self.primerNombrePasajero,self.primerApellidoPasajero)



# ###############################################################################################################################
# CREACIÓN DE LA TABLA (generarRuta) DE NUESTRA MER DISEÑADO EN MYSQL WORKBENCH
class GenerarRuta(models.Model):
    # FOREING KEY REREFENCIADA DEL MODELO ACTIVOS DE LAS CLASES REQUERIDAS VEHICULO, USUARIO Y PASAJERO.
    fkVehiculo=models.ForeignKey(ActivoVehiculo, on_delete=models.CASCADE, verbose_name="Vehículo", blank=True)
    fkUsuario=models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario", blank=True)
    horaSalida=models.TimeField(verbose_name="Hora de Salida", help_text="HH:MM", blank=True)
    horaRegreso=models.TimeField(verbose_name="Hora de Regreso", help_text="HH:MM")
<<<<<<< Updated upstream
    fechaSalida=models.DateField(verbose_name="Fecha de Salida", help_text="MM/DD/AAAA", blank=True)
    fechaRegreso=models.DateField(verbose_name="Fecha de Regreso", help_text="MM/DD/AAAA", blank=True)
    lugarSalida=models.CharField(max_length=50, verbose_name="Lugar de Salida", blank=True)
    lugarDestino=models.CharField(max_length=50, verbose_name="Lugar de Destino", blank=True)
    kilometrajeFinalVehiculo=models.IntegerField(verbose_name="Kilometraje Final", blank=True)  # Valor numero (IntegerField) Para sumar Kilometraje!!!!!!
    # fkDetalleRuta=models.ForeignKey(DetalleRuta, on_delete=models.CASCADE, verbose_name="Pasajero")
    descripcionRuta=models.TextField(max_length=100, verbose_name="Descripción", blank=True)
    observacionesRuta=models.TextField(max_length=100, verbose_name="Observaciones", blank=True)


# ###############################################################################################################################
class DetalleRuta(models.Model):
    fkRuta=models.ForeignKey(GenerarRuta, on_delete=models.CASCADE, verbose_name="Ruta")
    fkPasajero=models.ForeignKey(Pasajero, on_delete=models.CASCADE, verbose_name="Pasajero")
=======
    fechaSalida=models.DateField(verbose_name="Fecha de Salida", help_text="MM/DD/AAAA")
    fechaRegreso=models.DateField(verbose_name="Fecha de Regreso", help_text="MM/DD/AAAA")
    lugarSalida=models.CharField(max_length=50, verbose_name="Lugar de Salida")
    lugarDestino=models.CharField(max_length=50, verbose_name="Lugar de Destino")
    kilometrajeFinalVehiculo=models.IntegerField(verbose_name="Kilometraje Final")  # Valor numero (IntegerField) Para sumar Kilometraje!!!!!!
    descripcionRuta=models.TextField(max_length=100, verbose_name="Descripción")
    observacionesRuta=models.TextField(max_length=100, verbose_name="Observaciones")
>>>>>>> Stashed changes

class DetalleRuta(models.Model):
    fkRuta=models.ForeignKey(GenerarRuta, on_delete=models.CASCADE, verbose_name="Ruta")
    fkPasajero=models.ForeignKey(Pasajero, on_delete=models.CASCADE, verbose_name="Pasajero")

class DetalleRuta(models.Model):
    fkRuta=models.ForeignKey(GenerarRuta, on_delete=models.CASCADE, verbose_name="Ruta")
    fkPasajero=models.ForeignKey(Pasajero, on_delete=models.CASCADE, verbose_name="Pasajero")


# ###############################################################################################################################
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

# HACER 3 MODELOS PARA MANTENIMIENTO DE CADA ACTIVO - INDIVIDUAL
# añadir una tabla intermedia donde se registre el activo que quiero asociarle un mantenimiento. ---------------------------------
