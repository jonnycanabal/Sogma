from django.utils.translation import gettext_lazy as _
from enum import unique
from django.db import models

# Create your models here.

# CREACIÓN DE LA TABLA (activoExtintor) DE NUESTRA MER DISEÑADO EN MYSQL WORKBENCH
class ActivoExtintor(models.Model):
    serialExtintor=models.CharField(max_length=50, verbose_name="Serial Extintor")
    colorExtintor=models.CharField(max_length=20, verbose_name="Color Extintor")
    ubicacionExtintor=models.CharField(max_length=50, verbose_name="Ubicación del Extintor")
    class TipoExtintor(models.TextChoices):
        A='A', _("Tipo A")
        B='B', _("Tipo B")
        C='C', _("Tipo C")
        D='D', _("Tipo C")
    tipoExtintor=models.CharField(max_length=5, choices=TipoExtintor.choices, default=TipoExtintor.A, verbose_name="Tipo de Extintor")
    pesoExtintor=models.CharField(max_length=10, verbose_name="Peso del Extintor")

# CREACIÓN DE LA TABLA (activoEquipoOficina) DE NUESTRA MER DISEÑADO EN MYSQL WORKBENCH
class ActivoEquipoOficina(models.Model):
    serialEquipo=models.CharField(max_length=50, verbose_name="Serial Equipo")
    marcaEquipo=models.CharField(max_length=20, verbose_name="Marca Equipo")
    colorEquipo=models.CharField(max_length=20, verbose_name="Color Equipo")
    sistemaOperativo=models.CharField(max_length=20, default="No Aplica", verbose_name="Sistema Operativo")
    ramEquipo=models.CharField(max_length=20, default="No Aplica", verbose_name="Ram del Equipo")
    memoriaEquipo=models.CharField(max_length=20, default="No Aplica", verbose_name="Memoria del Equipo")
    ubicacionEquipo=models.CharField(max_length=50, verbose_name="Ubicación del Equipo")
    componentesAdicionales=models.TextField(max_length=100, verbose_name="Componentes del Equipo")
    class Estado(models.TextChoices):
        ACTIVO='1', _("Activo")
        INACTIVO='0', _("Inactivo")
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

# CREACIÓN DE LA TABLA (activoVehiculo) DE NUESTRA MER DISEÑADO EN MYSQL WORKBENCH
class ActivoVehiculo(models.Model):
    marcaVehiculo=models.CharField(max_length=20, verbose_name="Marca del Vehículo")
    modeloVehiculo=models.CharField(max_length=10, verbose_name="Modelo del Vehículo")
    placaVehiculo=models.CharField(max_length=10, unique=True, verbose_name="Placa del Vehículo") #Tiene campo Único
    colorVehiculo=models.CharField(max_length=20, verbose_name="Color del Vehículo")
    serialVehiculo=models.CharField(max_length=50, verbose_name="Serial del Vehiculo")
    tipoCombustible=models.CharField(max_length=20, verbose_name="Tipo de Combustible")
    cantidadPasajeros=models.CharField(max_length=5, verbose_name="Cantidad de Pasajeros")
    personaEncargadaVehiculo=models.CharField(max_length=50, verbose_name="Persona a Cargo")
    class Estado (models.TextChoices):
        NUEVO='Nuevo', _("Nuevo")
        USADO='Usado', _("Usado")
    estadoVehiculo=models.CharField(max_length=10, choices=Estado.choices, default=Estado.NUEVO, verbose_name="Estado del Vehículo")
    fechaIngresoVehiculo=models.DateField(verbose_name="Fecha de Ingreso", help_text="MM/DD/AAAA")
    fechaInicioSoat=models.DateField(verbose_name="Fecha Inicio Soat", help_text="MM/DD/AAAA")
    fechaFinSoat=models.DateField(verbose_name="Fecha Vencimiento Soat", help_text="MM/DD/AAAA")
    fechaInicioTecnicomecanica=models.DateField(verbose_name="Fecha Inicio Tecnicomecanica", help_text="MM/DD/AAAA")
    fechaVencimientoTecnicomecanica=models.DateField(verbose_name="Fecha Vencimiento Tecnicomecanica", help_text="MM/DD/AAAA")
    class Estado(models.TextChoices):
        ACTIVO='1', _("Activo")
        INACTIVO='0', _("Inactivo")
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

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
    primerApellidoPasajero=models.CharField(max_length=50, verbose_name="Primer Apellido")
    direccionPasajero=models.CharField(max_length=100, verbose_name="Dirección Residencia")
    telefonoPasajero=models.CharField(max_length=20, verbose_name="Teléfono")