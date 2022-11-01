from tabnanny import verbose
from venv import create
from django.utils.translation import gettext_lazy as _
from enum import unique
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# CREACIÓN DE LA TABLA (usuario) DE NUESTRA MER DISEÑADO EN MYSQL WORKBENCH
class Usuario(models.Model):
    primerNombre=models.CharField(max_length=50, verbose_name="Primer Nombre")
    segundoNombre=models.CharField(max_length=50, verbose_name="Segundo Nombre", blank=True)
    primerApellido=models.CharField(max_length=50, verbose_name="Primer Apellido")
    segundoApellido=models.CharField(max_length=50, verbose_name="Segundo Apellido", blank=True)
    foto=models.ImageField(upload_to='media/usuarios', blank=True, default='media/usuarios/default.jpg') # pip install pillow
    class TipoDocumento(models.TextChoices):
        CC='C.C.', _("Cédula de Ciudadania")
        CE='C.E.', _("Cédula de Extranjería")
        PASS='PASS', _("Pasaporte")
    tipoDocumento=models.CharField(max_length=5, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de Documento")
    numeroDocumento=models.CharField(max_length=50, unique=True, verbose_name="Número de Documento") #Tiene campo Único
    numeroTelefono=models.CharField(max_length=20, verbose_name="Número de Teléfono")
    ciudadResidencia=models.CharField(max_length=50, verbose_name="Ciudad de Residencia")
    direccionResidencia=models.CharField(max_length=100, verbose_name="Dirección de Residencia")
    correoElectronico=models.EmailField(max_length=100, verbose_name="Correo Electronico")
    class Genero(models.TextChoices):
        MASCULINO='Masculino', _("Masculino")
        FEMENINO='Femenino', _("Femenino")
        OTRO='Otro', _("Otro")
        NODECIR='Prefiero no decir', _("Prefiero no decir")
    genero=models.CharField(max_length=20, choices=Genero.choices, default=Genero.OTRO, verbose_name="Genero")
    cargo=models.CharField(max_length=30, verbose_name="Cargo")

    # Pendiente Usuario y Contraseña  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    fechaRegistro=models.DateField(verbose_name="Fecha de Registro", help_text="MM/DD/AAAA")
    class TipoUsuario(models.TextChoices):
        FUNCIONARIO='Funcionario', _("Funcionario")
        CONDUCTOR='Conductor', _("Conductor")
        ADMINISTRADOR='Administrador', _("Administrador")
    tipoUsuario=models.CharField(max_length=20, choices=TipoUsuario.choices, default=TipoUsuario.FUNCIONARIO, verbose_name="Tipo de Usuario")

    # Pendiente el tipo de dato SET como se manejaria para los permisos de usuario.
    # permisos=models.
    # class Permisos(models.Model):
    #     tags={'Consultar', 'Editar', 'Guardar', 'Eliminar', 'Nuevo Activo', 'Generar Reporte', 
    #     'Control Activos Todos', 'Control Activos Extintores', 'Control Activos Vehículos', 'Control Activos Equipo de Oficina', 
    #     'Todas las Páginas', 'Página [control-activos]', 'Página [generar-alarma]', 'Página [generar-ruta]', 'Página [consultar-ruta]'}

    class Estado(models.TextChoices):
        ACTIVO='1', _("Activo")
        INACTIVO='0', _("Inactivo")
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    user=models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return "%s %s" %(self.primerNombre, self.primerApellido)
