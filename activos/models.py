from django.utils.translation import gettext_lazy as _
from enum import unique
from django.db import models
from datetime import date

# Create your models here.

# CREACIÓN DE LA TABLA (activoExtintor) DE NUESTRA MER DISEÑADO EN MYSQL WORKBENCH
class ActivoExtintor(models.Model):
    fotoExtintor=models.ImageField(upload_to='extintores', blank=True, default='extintores/extintores_default.jpg') # pip install pillow
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
    fechaUltimaRecarga=models.DateField(verbose_name="Fecha Ultima Recarga", help_text="DD/MM/AAAA", default=date.today)
    # fechaProximaRecarga=models.DateField(verbose_name="Fecha Proxima Recarga", help_text="DD/MM/AAAA", default=date.today)
    class EstadoExtintor(models.TextChoices):
        ACTIVO='Activo', _("Activo")
        INACTIVO='Inactivo', _("Inactivo")
    estadoExtintor=models.CharField(max_length=10, choices=EstadoExtintor.choices, default=EstadoExtintor.ACTIVO, verbose_name="Estado")
    def __str__(self):
        return "%s" %(self.serialExtintor)

# CREACIÓN DE LA TABLA (activoEquipoOficina) DE NUESTRA MER DISEÑADO EN MYSQL WORKBENCH
class ActivoEquipoOficina(models.Model):
    fotoEquipo=models.ImageField(upload_to='equipos', blank=True, default='equipos/equipo_default.jpg') # pip install pillow
    serialEquipo=models.CharField(max_length=50, verbose_name="Serial Equipo")
    marcaEquipo=models.CharField(max_length=20, verbose_name="Marca Equipo")
    colorEquipo=models.CharField(max_length=20, verbose_name="Color Equipo")
    sistemaOperativo=models.CharField(max_length=20, verbose_name="Sistema Operativo", blank=True)
    ramEquipo=models.CharField(max_length=20, verbose_name="Ram del Equipo", blank=True)
    memoriaEquipo=models.CharField(max_length=20, verbose_name="Memoria del Equipo", blank=True)
    ubicacionEquipo=models.CharField(max_length=50, verbose_name="Ubicación del Equipo")
    # fechaProximaRevision=models.DateField(verbose_name="Fecha Proxima Revisión", help_text="DD/MM/AAAA", default=date.today)
    componentesAdicionales=models.TextField(max_length=100, verbose_name="Componentes del Equipo", blank=True)
    class EstadoEquipo(models.TextChoices):
        ACTIVO='Activo', _("Activo")
        INACTIVO='Inactivo', _("Inactivo")
    estadoEquipo=models.CharField(max_length=10, choices=EstadoEquipo.choices, default=EstadoEquipo.ACTIVO, verbose_name="Estado")
    def __str__(self):
        return "%s" %(self.marcaEquipo)

# CREACIÓN DE LA TABLA (activoVehiculo) DE NUESTRA MER DISEÑADO EN MYSQL WORKBENCH
class ActivoVehiculo(models.Model):
    fotoVehiculo=models.ImageField(upload_to='vehiculos', blank=True, default='vehiculos/vehiculo_default.jpg') # pip install pillow
    marcaVehiculo=models.CharField(max_length=20, verbose_name="Marca del Vehículo")
    modeloVehiculo=models.CharField(max_length=10, verbose_name="Modelo del Vehículo")
    placaVehiculo=models.CharField(max_length=10, unique=True, verbose_name="Placa del Vehículo") #Tiene campo Único
    colorVehiculo=models.CharField(max_length=20, verbose_name="Color del Vehículo")
    serialVehiculo=models.CharField(max_length=50, verbose_name="Serial del Vehiculo")
    tipoCombustible=models.CharField(max_length=20, verbose_name="Tipo de Combustible")
    cantidadPasajeros=models.CharField(max_length=5, verbose_name="Cantidad de Pasajeros")
    personaEncargadaVehiculo=models.CharField(max_length=50, verbose_name="Persona a Cargo")
    class CondicionVehiculo (models.TextChoices):
        NUEVO='Nuevo', _("Nuevo")
        USADO='Usado', _("Usado")
    condicionVehiculo=models.CharField(max_length=10, choices=CondicionVehiculo.choices, default=CondicionVehiculo.NUEVO, verbose_name="Condicion del Vehículo")
    fechaIngresoVehiculo=models.DateField(verbose_name="Fecha de Ingreso", help_text="DD/MM/AAAA")
    fechaInicioSoat=models.DateField(verbose_name="Fecha Inicio Soat", help_text="DD/MM/AAAA")
    fechaFinSoat=models.DateField(verbose_name="Fecha Vencimiento Soat", help_text="DD/MM/AAAA")
    fechaInicioTecnicomecanica=models.DateField(verbose_name="Fecha Inicio Tecnicomecanica", help_text="DD/MM/AAAA")
    fechaVencimientoTecnicomecanica=models.DateField(verbose_name="Fecha Vencimiento Tecnicomecanica", help_text="DD/MM/AAAA")
    # fechaProximoMantenimiento=models.DateField(verbose_name="Fecha Proximo Mantenimiento", help_text="DD/MM/AAAA", default=date.today)
    class EstadoVehiculo(models.TextChoices):
        ACTIVO='Activo', _("Activo")
        INACTIVO='Inactivo', _("Inactivo")
    estadoVehiculo=models.CharField(max_length=10, choices=EstadoVehiculo.choices, default=EstadoVehiculo.ACTIVO, verbose_name="Estado")
    def __str__(self):
        return "%s" %(self.placaVehiculo)