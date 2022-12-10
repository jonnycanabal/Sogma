from django.shortcuts import render

from gestionActivos.models import GenerarRuta, MantenimientoVehiculo, MantenimientoExtintor, MantenimientoEquipo
from activos.models import ActivoExtintor, ActivoVehiculo, ActivoEquipoOficina

import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from io import BytesIO


from django.conf import settings
from django.core.mail import send_mail
import threading
import time

from datetime import datetime, date

from django.views.defaults import page_not_found

from django.db.models import Sum

# views de la pagina de Inicio - Index


# Bloque de código con la función para generar el reporte de los vehículos por medio de una página en html
def reporte_vehiculo (request, pk):
        vehiculo = ActivoVehiculo.objects.get(id=pk)
        ultimoMantenimientoVehiculo=MantenimientoVehiculo.objects.filter(fkVehiculo=vehiculo).order_by('-fkRegistrarMantenimiento__fechaMantenimiento')
        mantenimientos= MantenimientoVehiculo.objects.filter(fkVehiculo=vehiculo)
        if ultimoMantenimientoVehiculo:
            ultimoMantenimientoVehiculo = ultimoMantenimientoVehiculo[0]
        else:
            ultimoMantenimientoVehiculo = None
        
        kilometraje=GenerarRuta.objects.filter(fkVehiculo=vehiculo).order_by('-fechaRegreso', '-horaRegreso')
        if kilometraje:
            kilometraje=kilometraje[0]
        else:
            kilometraje = None

        total= mantenimientos.aggregate(total_precio=Sum('fkRegistrarMantenimiento__valorMantenimiento'))

        # template = get_template('reportes/reporte_vehiculo.html')
        context = {
            'title': 'Reporte Vehiculo',
            'vehiculo':vehiculo,
            'ultimoMantenimientoVehiculo':ultimoMantenimientoVehiculo,
            'kilometraje':kilometraje,
            # 'vehiculo': ActivoVehiculo.objects.get(id=pk),
            'mantenimientos': mantenimientos,
            'total':total['total_precio'],
            }

        return render (request, 'reportes/reporte_vehiculo.html', context)


# Bloque de código con la función para generar el reporte de los extintores por medio de una página en html
def reporte_extintor (request, pk):
        extintor = ActivoExtintor.objects.get(id=pk)
        mantenimientos = MantenimientoExtintor.objects.filter(fkExtintor=extintor)
        ultimoMantenimientoExtintor=MantenimientoExtintor.objects.filter(fkExtintor=extintor).order_by('-fkRegistrarMantenimiento__fechaMantenimiento')
        if ultimoMantenimientoExtintor:
            ultimoMantenimientoExtintor = ultimoMantenimientoExtintor[0]
        else:
            ultimoMantenimientoExtintor = None
        
        total = mantenimientos.aggregate(total_precio=Sum('fkRegistrarMantenimiento__valorMantenimiento'))

        context = {
            'title': 'Reporte Extintor',
            'extintor':extintor,
            'ultimoMantenimientoExtintor':ultimoMantenimientoExtintor,
            'mantenimientos': mantenimientos,
            'total':total['total_precio']
            }

        return render (request, 'reportes/reporte_extintor.html', context)


# Bloque de código con la función para generar el reporte de los equipos de oficina por medio de una página en html
def reporte_equipo (request, pk):
        equipo = ActivoEquipoOficina.objects.get(id=pk)
        mantenimientos = MantenimientoEquipo.objects.filter(fkEquipoOficina=equipo)
        ultimoMantenimientoEquipo=MantenimientoEquipo.objects.filter(fkEquipoOficina=equipo).order_by('-fkRegistrarMantenimiento__fechaMantenimiento')
        if ultimoMantenimientoEquipo:
            ultimoMantenimientoEquipo = ultimoMantenimientoEquipo[0]
        else:
            ultimoMantenimientoEquipo = None
        
        total= mantenimientos.aggregate(total_precio=Sum('fkRegistrarMantenimiento__valorMantenimiento'))
        context = {
            'title': 'Reporte Equipo',
            'equipo':equipo,
            'ultimoMantenimientoEquipo':ultimoMantenimientoEquipo,
            'mantenimientos': mantenimientos,
            'total':total['total_precio']
            }

        return render (request, 'reportes/reporte_equipo.html', context)


def error_404(request, exception):
    return page_not_found(request, '404.html')



def error_500(request):
    return render (request, '500.html')

def informacion(request):
    title='información'

    context ={
        'title':title
    }
    return render (request, 'informacion.html', context)




def inicio (request):

    titulo = 'Index'
    context = {
        'titulo': titulo
    }

    return render (request, 'index.html', context)

# views de la pagina de Control Activos
def control_activos (request):

    titulo = 'Control-Activos'
    context = {
        'titulo': titulo
    }

    return render (request,'controlActivos.html', context)

# views de la pagina Generar Alarma
def generar_alarma (request):

    titulo = 'Generar-Alarma'
    context = {
        'titulo': titulo
    }

    return render (request, 'generarAlarma.html', context)

# views de la pagina de Generar Ruta
def generar_ruta (request):

    titulo = 'Generar-Ruta'
    context = {
        'titulo': titulo
    }

    return render (request, 'generarRuta.html', context)

# views de la pagina de Consultar Ruta
def consultar_ruta (request):
    rutas= GenerarRuta.objects.all() #Esto mismo de establece para los vehiculos
    titulo = 'Consultar-Ruta'
    context = {
        'titulo': titulo,
        'rutas': rutas
    }

    return render (request, 'consultarRuta.html', context)

# views de la pagina de Nuevo Usuario
def nuevo_usuario (request):

    titulo = 'Nuevo-Usuario'
    context = {
        'titulo': titulo
    }

    return render (request, 'nuevoUsuario.html')

# views de la pagina de Registrar Mantenimiento
def registrar_mantenimiento (request):

    titulo = 'Registrar-Mantenimiento'
    context = {
        'titulo': titulo
    }

    return render (request, 'registrarMantenimiento.html', context)