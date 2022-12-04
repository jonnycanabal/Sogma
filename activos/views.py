from email import message
from multiprocessing import context
from django.shortcuts import redirect, render
from activos.models import ActivoEquipoOficina, ActivoExtintor, ActivoVehiculo
from activos.forms import ActivoEquipoOficinaForm, ActivoExtintorForm, ActivoVehiculoForm, ActivoVehiculoEditarForm, ActivoExtintorEditarForm, ActivoEquipoOficinaEditarForm
from gestionActivos.models import MantenimientoVehiculo, GenerarRuta, MantenimientoExtintor, MantenimientoEquipo
from django.contrib import messages

# Importe con el cual habilitamos el @login_required
from django.contrib.auth.decorators import login_required
# Importe para logout en la funcion logout_user
from django.contrib.auth import logout 

# Create your views here.

@login_required(login_url='login')
def control_activos(request):
    titulo='control-activos'
    extintores= ActivoExtintor.objects.filter(estadoExtintor="Activo")
    vehiculos=ActivoVehiculo.objects.filter(estadoVehiculo="Activo")
    equipos=ActivoEquipoOficina.objects.filter(estadoEquipo="Activo")
    ultimoMantenimientoVehiculo=None
    ultimoMantenimientoExtintor=None
    ultimoMantenimientoEquipo=None
    kilometraje=None
    # form=ActivoExtintorForm()
    # form=ActivoVehiculoForm()
    # form=ActivoEquipoOficinaForm()
    extintor=None
    vehiculo=None
    equipo=None



# ###################################################################################################################################
    # Bloque de codigo para traer informacion de la tabla a los campos de la pagina html por medio de la Primary Key
    if request.method == "POST" and 'editar-extintor' in request.POST:
        extintor = ActivoExtintor.objects.get(id=int(request.POST['pk_extintor']))
        ultimoMantenimientoExtintor=MantenimientoExtintor.objects.filter(fkExtintor=extintor).order_by('-fkRegistrarMantenimiento__fechaMantenimiento')
        if ultimoMantenimientoExtintor:
            ultimoMantenimientoExtintor = ultimoMantenimientoExtintor[0]
        else:
            ultimoMantenimientoExtintor = None

    if request.method == "POST" and 'editar-vehiculo' in request.POST:
        vehiculo = ActivoVehiculo.objects.get(id=int(request.POST['pk_vehiculo']))
        ultimoMantenimientoVehiculo=MantenimientoVehiculo.objects.filter(fkVehiculo=vehiculo).order_by('-fkRegistrarMantenimiento__fechaMantenimiento')
        if ultimoMantenimientoVehiculo:
            ultimoMantenimientoVehiculo = ultimoMantenimientoVehiculo[0]
        else:
            ultimoMantenimientoVehiculo = None
        
        kilometraje=GenerarRuta.objects.filter(fkVehiculo=vehiculo).order_by('-fechaRegreso', '-horaRegreso')
        if kilometraje:
            kilometraje = kilometraje[0]
        else:
            kilometraje = None

    if request.method == "POST" and 'editar-equipo-oficina' in request.POST:
        equipo = ActivoEquipoOficina.objects.get(id=int(request.POST['pk_equipo']))
        ultimoMantenimientoEquipo=MantenimientoEquipo.objects.filter(fkEquipoOficina=equipo).order_by('-fkRegistrarMantenimiento__fechaMantenimiento')
        if ultimoMantenimientoEquipo:
            ultimoMantenimientoEquipo = ultimoMantenimientoEquipo[0]
        else:
            ultimoMantenimientoEquipo = None

# ###################################################################################################################################
    # Bloque de codigo para editar los activos Extintor - Vehiculos - Equipos de Oficina
    # EDITAR VEHÍCULO
    if request.method == "POST" and 'c-editar-vehiculo' in request.POST:
        print("######################", request.POST)
        vehiculo = ActivoVehiculo.objects.get(id=int(request.POST['pk_vehiculo']))
        form=ActivoVehiculoEditarForm(request.POST, request.FILES, instance=vehiculo)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"SE EDITÓ EL VEHÍCULO CON ID # {vehiculo.id} EXITOSAMENTE"
            )
        else:
            # form=ActivoVehiculoEditarForm(request.POST, request.FILES, instance=vehiculo)
            # print (form.errors)
            messages.error(
                request,f"ERROR NO SE EDITÓ EL VEHÍCULO CON ID # {vehiculo.id} "
            )

    # EDITAR EXTINTOR
    if request.method == "POST" and 'c-editar-extintor' in request.POST:
        print("######################", request.POST)
        extintor = ActivoExtintor.objects.get(id=int(request.POST['pk_extintor']))
        form=ActivoExtintorEditarForm(request.POST, request.FILES, instance=extintor)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"SE EDITÓ EL EXTINTOR CON ID # {extintor.id} EXITOSAMENTE"
            )
        else:
            messages.error(
                request,f"ERROR NO SE EDITÓ EL EXTINTOR CON ID # {extintor.id} "
            )
            print("error editar extintor")

    # EDITAR EQUIPO DE OFICINA
    if request.method == "POST" and 'c-editar-equipo' in request.POST:
        print("######################", request.POST)
        equipo = ActivoEquipoOficina.objects.get(id=int(request.POST['pk_equipo']))
        form=ActivoEquipoOficinaEditarForm(request.POST, request.FILES, instance=equipo)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"SE EDITÓ EL EQUIPO DE OFICINA CON ID # {equipo.id} EXITOSAMENTE"
            )
        else:
            messages.error(
                request,f"ERROR NO SE EDITÓ EL EQUIPO DE OFICINA CON ID # {equipo.id} "
            )
            print("error editar equipo de oficina")


# ###################################################################################################################################
    # CAPTURAR INFORMACION EN EL WIZARD PARA REGISTRAR ACTIVOS.
    if request.method == "POST" and 'form-extintor' in request.POST:
        form=ActivoExtintorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('###################################### EXTINTOR CREADO')
            messages.success(
            request,f"SE REGISTRÓ EL EXTINTOR EXITOSAMENTE"
        )
        else:
            print('######################################', form.errors)
            form=ActivoExtintorForm(request.POST)
            print('###################################### EXTINTOR ERROR')
            messages.error(
            request,f"ERROR, YA EXISTE UN EXTINTOR CON ESE NÚMERO DE SERIAL"
        )

    if request.method == "POST" and 'form-oficina' in request.POST:
        form=ActivoEquipoOficinaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('###################################### EQUIPO CREADO')
            messages.success(
            request,f"SE REGISTRÓ EL EQUIPO DE OFICINA EXITOSAMENTE"
        )
        else:
            print('######################################', form.errors)
            form=ActivoEquipoOficinaForm(request.POST)
            print('###################################### EQUIPO ERROR')
            messages.error(
            request,f"ERROR, YA EXISTE UN EQUIPO DE OFICINA CON ESE NÚMERO DE SERIAL"
        )

    if request.method == "POST" and 'form-vehiculo' in request.POST:
        form=ActivoVehiculoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('###################################### VEHICULO CREADO')
            messages.success(
            request,f"SE REGISTRÓ EL VEHÍCULO EXITOSAMENTE"
        )
        else:
            print('######################################', form.errors)
            form=ActivoVehiculoForm(request.POST)
            print('###################################### VEHICULO ERROR')
            messages.error(
            request,f"ERROR, YA EXISTE UN VEHÍCULO CON ESE NÚMERO DE PLACA Y/O SERIAL"
        )
    context={
        'titulo':titulo,
        'extintores':extintores,
        'extintor':extintor,
        'vehiculos':vehiculos,
        'vehiculo':vehiculo,
        'equipos':equipos,
        'equipo':equipo,
        'ultimoMantenimientoVehiculo':ultimoMantenimientoVehiculo,
        'ultimoMantenimientoExtintor':ultimoMantenimientoExtintor,
        'ultimoMantenimientoEquipo':ultimoMantenimientoEquipo,
        'kilometraje':kilometraje,
        # 'form':form 
    }
    return render (request, 'activos/controlActivos.html', context)


# ###################################################################################################################################
# FUNCIONES PARA ELIMINAR O INHABILITAR LOS VEHICULOS
@login_required(login_url='login')
def control_activos_eliminar_vehiculo(request,pk):
    titulo = 'control-activos'
    vehiculos=ActivoVehiculo.objects.all()

    # Bloque de codigo para ELIMINAR O DESACTIVAR UN ACTIVO
    ActivoVehiculo.objects.filter(id=pk).update(
        estadoVehiculo='Inactivo'
    )
    messages.success(
            request,f"SE ELIMINÓ EL VEHÍCULO EXITOSAMENTE"
        )

    return redirect('control-activos')

    context ={
        'titulo':titulo,
        'vehiculos':vehiculos,
    }

    return render (request, 'activos/controlActivos.html', context)

# ###################################################################################################################################
# FUNCIONES PARA ELIMINAR O INHABILITAR LOS EXTINTORES
@login_required(login_url='login')
def control_activos_eliminar_extintor(request,pk):
    # Bloque de codigo para ELIMINAR O DESACTIVAR UN ACTIVO
    ActivoExtintor.objects.filter(id=pk).update(
        estadoExtintor='Inactivo'       
    )
    messages.success(
            request,f"SE ELIMINÓ EL EXTINTOR EXITOSAMENTE"
        )

    return redirect('control-activos')
    
    context ={
        'titulo':titulo,
        'vehiculos':vehiculos,
    }

    return render (request, 'activos/controlActivos.html', context)
    
# ###################################################################################################################################
# FUNCIONES PARA ELIMINAR O INHABILITAR LOS EQUIPOS DE OFICINA
@login_required(login_url='login')
def control_activos_eliminar_equipo(request,pk):
    titulo = 'control-activos'
    equipos=ActivoEquipoOficina.objects.all()

    # Bloque de codigo para ELIMINAR O DESACTIVAR UN ACTIVO
    ActivoEquipoOficina.objects.filter(id=pk).update(
        estadoEquipo='Inactivo'
    )
    messages.success(
            request,f"SE ELIMINÓ EL EQUIPO DE OFICINA EXITOSAMENTE"
        )

    return redirect('control-activos')

    context ={
        'titulo':titulo,
        'equipos':equipos
    }

    return render (request, 'activos/controlActivos.html', context)

# Funcion para el Logout o cierre de sesión
def logout_user(request):
    logout(request)
    return redirect("login")