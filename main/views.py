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

# views de la pagina de Inicio - Index


# Bloque de código con la función para generar el reporte de los vehículos por medio de una página en html
def reporte_vehiculo (request, pk):
        vehiculo = ActivoVehiculo.objects.get(id=pk)
        # template = get_template('reportes/reporte_vehiculo.html')
        context = {
            'title': 'Reporte Vehiculo',
            'vehiculo':vehiculo,
            # 'vehiculo': ActivoVehiculo.objects.get(id=pk),
            'mantenimientos': MantenimientoVehiculo.objects.filter(fkVehiculo=vehiculo)
            
            }
        # response = HttpResponse(content_type='application/pdf')
        # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        # html = template.render(context)
        # result = BytesIO()
        # pdf = pisa.pisaDocument(BytesIO(html.encode('ISO-8859-1')), result)

        # pisa_status = pisa.CreatePDF(
        #     html, dest=response)
        # if error then show some funny view
        # if pisa_status.err:
        #     return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return render (request, 'reportes/reporte_vehiculo.html', context)


# Bloque de código con la función para generar el reporte de los extintores por medio de una página en html
def reporte_extintor (request, pk):
        extintor = ActivoExtintor.objects.get(id=pk)
        # template = get_template('reportes/reporte_vehiculo.html')
        context = {
            'title': 'Reporte Vehiculo',
            'extintor':extintor,
            # 'vehiculo': ActivoVehiculo.objects.get(id=pk),
            'mantenimientos': MantenimientoExtintor.objects.filter(fkExtintor=extintor)
            
            }

        return render (request, 'reportes/reporte_extintor.html', context)


# Bloque de código con la función para generar el reporte de los equipos de oficina por medio de una página en html
def reporte_equipo (request, pk):
        equipo = ActivoEquipoOficina.objects.get(id=pk)
        # template = get_template('reportes/reporte_vehiculo.html')
        context = {
            'title': 'Reporte Vehiculo',
            'equipo':equipo,
            # 'vehiculo': ActivoVehiculo.objects.get(id=pk),
            'mantenimientos': MantenimientoEquipo.objects.filter(fkEquipoOficina=equipo)
            
            }

        return render (request, 'reportes/reporte_equipo.html', context)



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