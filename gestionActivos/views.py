from multiprocessing import context
from django.shortcuts import render,redirect
from activos.models import ActivoEquipoOficina, ActivoExtintor, ActivoVehiculo
from gestionActivos.models import GenerarRuta
from gestionActivos.forms import GenerarAlarmaForm, GenerarRutaForm, RegistrarMantenimientoForm
from usuarios.models import Usuario
from django.contrib import messages

# Create your views here.

# ##################################################################################################################################
# FUNCION * GENERAR ALARMA *
def generar_alarma(request):
    titulo='Generar-Alarma'
    form=GenerarAlarmaForm()
    context={
        'titulo':titulo,
        'form':form
    }
    return render (request, 'gestionActivos/generarAlarma.html', context)

# ##################################################################################################################################
# FUNCION * GENERAR RUTA *
def generar_ruta(request):
    titulo='Consultar-Ruta'
    ruta=None
    vehiculos=ActivoVehiculo.objects.all()
    usuarios=Usuario.objects.all()
    # BLoque para guardar el formulario de generar ruta
    form=GenerarRutaForm(request.POST)
    if form.is_valid():
        form.save()
        print('###################################### EXTINTOR CREADO')
        messages.success(
            request,f"SE REGISTRO LA RUTA EXITOSAMENTE"
        )

    if request.method== 'POST':
        
        return redirect('agregar-ruta')

    context={
        'titulo':titulo,
        'vehiculos':vehiculos,
        'usuarios':usuarios,
        'form':form,
        'ruta':ruta
    }
    return render (request, 'gestionActivos/generarRuta.html', context)

# ##################################################################################################################################
# FUNCION * AGREGAR FUNCIONARIOS RUTA *
def agregar_funcionarios_ruta(request, pk):
    titulo='Consultar-Ruta'
    ruta= GenerarRuta.objects.get(id=pk)
    # pasajeros= DetalleRuta.objects.filter(fkRuta_id=pk)

    context={
        'titulo':titulo,
        # 'vehiculos':vehiculos,
        'ruta':ruta
    }
    return render (request, 'gestionActivos/generarRuta.html', context)

# def eliminar_pasajero(request):

#     context={

#     }

#     return render (request, 'gestionActivos/generarRuta.html', context)

# ##################################################################################################################################
# FUNCION * REGISTRAR MANTENIMIENTO *
def registrar_mantenimiento(request):
    titulo='Registrar-Mantenimiento'
    extintores= ActivoExtintor.objects.all()
    vehiculos=ActivoVehiculo.objects.all()
    equipos=ActivoEquipoOficina.objects.all()
    extintor=None
    vehiculo=None
    equipo=None

    # Bloque de codigo para traer informacion de la tabla a los campos de la pagina html por medio de la Primary Key
    if request.method == "POST" and 'editar-extintor' in request.POST:
        extintor = ActivoExtintor.objects.get(id=int(request.POST['pk_extintor']))

    if request.method == "POST" and 'editar-vehiculo' in request.POST:
        vehiculo = ActivoVehiculo.objects.get(id=int(request.POST['pk_vehiculo']))

    if request.method == "POST" and 'editar-equipo-oficina' in request.POST:
        equipo = ActivoEquipoOficina.objects.get(id=int(request.POST['pk_equipo']))

    form=RegistrarMantenimientoForm()
    
    context={
        'titulo':titulo,
        'extintores':extintores,
        'extintor':extintor,
        'vehiculos':vehiculos,
        'vehiculo':vehiculo,
        'equipos':equipos,
        'equipo':equipo,
        'form':form
    }
    return render (request, 'gestionActivos/registrarMantenimiento.html', context)

# ##################################################################################################################################
# FUNCION * CONSULTAR RUTA *
def consultar_ruta(request):
    titulo='Consultar-Ruta'
    extintores= ActivoExtintor.objects.all()
    vehiculos=ActivoVehiculo.objects.all()
    equipos=ActivoEquipoOficina.objects.all()
    vehiculo=None

    # Bloque de codigo para traer informacion de la tabla a los campos de la pagina html por medio de la Primary Key
    if request.method == "POST" and 'editar-vehiculo' in request.POST:
        vehiculo = ActivoVehiculo.objects.get(id=int(request.POST['pk_vehiculo']))

    context={
        'titulo':titulo,
        'extintores':extintores,
        'vehiculos':vehiculos,
        'vehiculo':vehiculo,
        'equipos':equipos

    }
    return render (request, 'gestionActivos/consultarRuta.html', context)