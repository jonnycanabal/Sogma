from multiprocessing import context
from django.shortcuts import render
from activos.models import ActivoEquipoOficina, ActivoExtintor, ActivoVehiculo

from gestionActivos.forms import GenerarAlarmaForm, GenerarRutaForm, RegistrarMantenimientoForm

# Create your views here.

def generar_alarma(request):
    titulo='Generar-Alarma'
    form=GenerarAlarmaForm()
    context={
        'titulo':titulo,
        'form':form
    }
    return render (request, 'gestionActivos/generarAlarma.html', context)

def generar_ruta(request):
    titulo='Consultar-Ruta'
    form=GenerarRutaForm()
    context={
        'titulo':titulo,
        'form':form
    }
    return render (request, 'gestionActivos/generarRuta.html', context)

def registrar_mantenimiento(request):
    titulo='Registrar-Mantenimiento'
    extintores= ActivoExtintor.objects.all()
    vehiculos=ActivoVehiculo.objects.all()
    equipos=ActivoEquipoOficina.objects.all()
    form=RegistrarMantenimientoForm()
    context={
        'titulo':titulo,
        'extintores':extintores,
        'vehiculos':vehiculos,
        'equipos':equipos,
        'form':form
    }
    return render (request, 'gestionActivos/registrarMantenimiento.html', context)