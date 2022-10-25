from email import message
from multiprocessing import context
from django.shortcuts import redirect, render
from activos.models import ActivoEquipoOficina, ActivoExtintor, ActivoVehiculo
from activos.forms import ActivoEquipoOficinaForm, ActivoExtintorForm, ActivoVehiculoForm
from django.contrib import messages
# Create your views here.

def control_activos(request):
    titulo='control-activos'
    extintores= ActivoExtintor.objects.filter(estadoExtintor="Activo")
    vehiculos=ActivoVehiculo.objects.filter(estadoVehiculo="Activo")
    equipos=ActivoEquipoOficina.objects.filter(estadoEquipo="Activo")
    # formExtintor=ActivoExtintorForm()
    # formVehiculo=ActivoVehiculoForm()
    # formEquipo=ActivoEquipoOficinaForm()
    extintor=None
    vehiculo=None
    equipo=None

# ###################################################################################################################################
    # Bloque de codigo para traer informacion de la tabla a los campos de la pagina html por medio de la Primary Key
    if request.method == "POST" and 'editar-extintor' in request.POST:
        extintor = ActivoExtintor.objects.get(id=int(request.POST['pk_extintor']))

    if request.method == "POST" and 'editar-vehiculo' in request.POST:
        vehiculo = ActivoVehiculo.objects.get(id=int(request.POST['pk_vehiculo']))

    if request.method == "POST" and 'editar-equipo-oficina' in request.POST:
        equipo = ActivoEquipoOficina.objects.get(id=int(request.POST['pk_equipo']))

# ###################################################################################################################################
    # Bloque de codigo para editar los activos Extintor - Vehiculos - Equipos de Oficina
    # EDITAR VEHÍCULO
    if request.method == "POST" and 'c-editar-vehiculo' in request.POST:
        print("######################", request.POST)
        vehiculo = ActivoVehiculo.objects.get(id=int(request.POST['pk_vehiculo']))
        form=ActivoVehiculoForm(request.POST,instance=vehiculo)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"SE EDITO EL VEHÍCULO CON ID # {vehiculo.id} EXITOSAMENTE"
            )
        else:
           messages.error(
                request,f"ERROR NO SE EDITO EL VEHÍCULO CON ID # {vehiculo.id} "
            )

    # EDITAR EXTINTOR
    if request.method == "POST" and 'c-editar-extintor' in request.POST:
        print("######################", request.POST)
        extintor = ActivoExtintor.objects.get(id=int(request.POST['pk_extintor']))
        form=ActivoExtintorForm(request.POST,instance=extintor)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"SE EDITO EL EXTINTOR CON ID # {extintor.id} EXITOSAMENTE"
            )
        else:
            print("error editar extintor")

    # EDITAR EQUIPO DE OFICINA
    if request.method == "POST" and 'c-editar-equipo' in request.POST:
        print("######################", request.POST)
        equipo = ActivoEquipoOficina.objects.get(id=int(request.POST['pk_equipo']))
        form=ActivoEquipoOficinaForm(request.POST,instance=equipo)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"SE EDITO EL EQUIPO DE OFICINA CON ID # {equipo.id} EXITOSAMENTE"
            )
        else:
            print("error editar equipo de oficina")


# ###################################################################################################################################
    # CAPTURAR INFORMACION EN EL WIZARD PARA REGISTRAR ACTIVOS.
    if request.method == "POST" and 'form-extintor' in request.POST:
        form=ActivoExtintorForm(request.POST)
        if form.is_valid():
            form.save()
            print('###################################### EXTINTOR CREADO')
            messages.success(
            request,f"SE REGISTRO EL EXTINTOR EXITOSAMENTE"
        )
        else:
            form=ActivoExtintorForm(request.POST)
            print('###################################### EXTINTOR ERROR')

    if request.method == "POST" and 'form-oficina' in request.POST:
        form=ActivoEquipoOficinaForm(request.POST)
        if form.is_valid():
            form.save()
            print('###################################### EQUIPO CREADO')
            messages.success(
            request,f"SE REGISTRO EL EQUIPO DE OFICINA EXITOSAMENTE"
        )
        else:
            form=ActivoEquipoOficinaForm(request.POST)
            print('###################################### EQUIPO ERROR')

    if request.method == "POST" and 'form-vehiculo' in request.POST:
        form=ActivoVehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            print('###################################### VEHICULO CREADO')
            messages.success(
            request,f"SE REGISTRO EL VEHÍCULO EXITOSAMENTE"
        )
        else:
            form=ActivoVehiculoForm(request.POST)
            print('###################################### VEHICULO ERROR')

    context={
        'titulo':titulo,
        'extintores':extintores,
        'extintor':extintor,
        'vehiculos':vehiculos,
        'vehiculo':vehiculo,
        'equipos':equipos,
        'equipo':equipo,
    }
    return render (request, 'activos/controlActivos.html', context)


# ###################################################################################################################################
# FUNCIONES PARA ELIMINAR O INHABILITAR LOS VEHICULOS
def control_activos_eliminar_vehiculo(request,pk):
    titulo = 'control-activos'
    vehiculos=ActivoVehiculo.objects.all()

    # Bloque de codigo para ELIMINAR O DESACTIVAR UN ACTIVO
    ActivoVehiculo.objects.filter(id=pk).update(
        estadoVehiculo='Inactivo'
    )
    messages.success(
            request,f"SE ELIMINO EL VEHICULO EXITOSAMENTE"
        )

    return redirect('control-activos')

    context ={
        'titulo':titulo,
        'vehiculos':vehiculos,
    }

    return render (request, 'activos/controlActivos.html', context)

# ###################################################################################################################################
# FUNCIONES PARA ELIMINAR O INHABILITAR LOS EXTINTORES
def control_activos_eliminar_extintor(request,pk):
    # Bloque de codigo para ELIMINAR O DESACTIVAR UN ACTIVO
    ActivoExtintor.objects.filter(id=pk).update(
        estadoExtintor='Inactivo'       
    )
    messages.success(
            request,f"SE ELIMINO EL EXTINTOR EXITOSAMENTE"
        )

    return redirect('control-activos')
    
    context ={
        'titulo':titulo,
        'vehiculos':vehiculos,
    }

    return render (request, 'activos/controlActivos.html', context)
    
# ###################################################################################################################################
# FUNCIONES PARA ELIMINAR O INHABILITAR LOS EQUIPOS DE OFICINA
def control_activos_eliminar_equipo(request,pk):
    titulo = 'control-activos'
    equipos=ActivoEquipoOficina.objects.all()

    # Bloque de codigo para ELIMINAR O DESACTIVAR UN ACTIVO
    ActivoEquipoOficina.objects.filter(id=pk).update(
        estadoEquipo='Inactivo'
    )
    messages.success(
            request,f"SE ELIMINO EL EQUIPO DE OFICINA EXITOSAMENTE"
        )

    return redirect('control-activos')

    context ={
        'titulo':titulo,
        'equipos':equipos
    }

    return render (request, 'activos/controlActivos.html', context)



# def control_activos_eliminar_vehiculo(request,pk):
#     titulo = 'control-activos'
#     extintores= ActivoExtintor.objects.all()
#     vehiculos=ActivoVehiculo.objects.all()
#     equipos=ActivoEquipoOficina.objects.all()

#     # Bloque de codigo para ELIMINAR O DESACTIVAR UN ACTIVO
#     ActivoExtintor.objects.filter(id=pk).update(
#         estadoExtintor='Inactivo'
#     )

#     ActivoVehiculo.objects.filter(id=pk).update(
#         estadoVehiculo='Inactivo'
#     )

#     ActivoEquipoOficina.objects.filter(id=pk).update(
#         estadoEquipo='Inactivo'
#     )

#     context ={
#         'titulo':titulo,
#         'extintores':extintores,
#         'vehiculos':vehiculos,
#         'equipos':equipos
#     }

#     return render (request, 'activos/controlActivos.html', context)