from multiprocessing import context
from django.shortcuts import render,redirect
from activos.models import ActivoEquipoOficina, ActivoExtintor, ActivoVehiculo
from gestionActivos.models import GenerarRuta, MantenimientoEquipo, MantenimientoExtintor, MantenimientoVehiculo, Pasajero, RegistrarMantenimiento
from gestionActivos.forms import GenerarAlarmaForm, GenerarRutaForm, PasajeroForm, RegistrarMantenimientoForm
from usuarios.models import Usuario
from django.contrib import messages

# Importe con el cual habilitamos el @login_required
from django.contrib.auth.decorators import login_required
# Importe para logout en la funcion logout_user
from django.contrib.auth import logout 


# Create your views here.

# ##################################################################################################################################
# FUNCION * GENERAR ALARMA *
@login_required(login_url='login')
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
@login_required(login_url='login')
def generar_ruta(request):
    titulo='Consultar-Ruta'
    ruta=None
    pasajeros= Pasajero.objects.all()

    vehiculos=ActivoVehiculo.objects.all()
    usuarios=Usuario.objects.all()
    # BLoque para guardar el formulario de generar ruta
    form=GenerarRutaForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(
            request,f"SE REGISTRO LA RUTA EXITOSAMENTE"
        )
        return redirect('agregar-ruta')

    if request.method== 'POST' and 'pasajero-buscar' in request.POST:
        return redirect('agregar-ruta')



    if request.method == "POST" and 'form-pasajero' in request.POST:
        form=PasajeroForm(request.POST)
        if form.is_valid():
            form.save()
            print('###################################### PASAJERO REGISTRADO')
            messages.success(
            request,f"SE REGISTRO EL PASAJERO EXITOSAMENTE"
        )
        else:
            form=PasajeroForm(request.POST)
            print('###################################### ERROR PASAJERO NO REGISTRADO')
            messages.error(
            request,f"ERROR. NO SE PUDO REGISTRAR AL PASAJERO. INTENTELO DE NUEVO"
        )


    context={
        'titulo':titulo,
        'vehiculos':vehiculos,
        'usuarios':usuarios,
        'form':form,
        'ruta':ruta,
        'pasajeros':pasajeros,
    }
    return render (request, 'gestionActivos/generarRuta.html', context)

def registrar_pasajero(request):

    context={

    }

    return render (request, 'gestionActivos/generarRuta.html', context)

# ##################################################################################################################################
# FUNCION * AGREGAR FUNCIONARIOS RUTA *
@login_required(login_url='login')
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
@login_required(login_url='login')
def registrar_mantenimiento(request):
    titulo='Registrar-Mantenimiento'
    extintores= ActivoExtintor.objects.all()
    vehiculos=ActivoVehiculo.objects.all()
    equipos=ActivoEquipoOficina.objects.all()
    extintor=None
    vehiculo=None
    equipo=None
    form=None
    # ##############################################################################################################
    # Bloque de codigo para traer informacion de la tabla a los campos de la pagina html por medio de la Primary Key
    if request.method == "POST" and 'editar-extintor' in request.POST:
        extintor = ActivoExtintor.objects.get(id=int(request.POST['pk_extintor']))

    if request.method == "POST" and 'editar-vehiculo' in request.POST:
        vehiculo = ActivoVehiculo.objects.get(id=int(request.POST['pk_vehiculo']))

    if request.method == "POST" and 'editar-equipo-oficina' in request.POST:
        equipo = ActivoEquipoOficina.objects.get(id=int(request.POST['pk_equipo']))


    # ############################################################################################################################
    # BLOQUE DE CODIGO PARA REGISTRAR MANTENIMIENTO CON VEHICULO
    if request.method == "POST" and 'r-mantenimiento-vehiculo' in request.POST:
        vehiculo=ActivoVehiculo.objects.get(id=int(request.POST['pk_vehiculo']))
        form=RegistrarMantenimientoForm(request.POST, request.FILES)
        if form.is_valid():
            registro=form.save()
            print(registro)
            detalle=MantenimientoVehiculo.objects.create(
                fkVehiculo=vehiculo,
                kilometrajeMantenimiento=request.POST['kilometrajeMantenimiento'],
                fkRegistrarMantenimiento=RegistrarMantenimiento.objects.get(id=registro.id)
            )
            messages.success(
                request, f"SE REGISTRO EL MANTENIMIENTO DEL VEHICULO EXITOSAMENTE"
            )
        else:
            messages.error(
                request, f"ERROR!!!, NO SE PUDO REGISTRAR EL MANTENIMIENTO DEL VEHICULO"
            )

    # ############################################################################################################################
    # BLOQUE DE CODIGO PARA REGISTRAR MANTENIMIENTO CON EXTINTOR
    if request.method == "POST" and 'r-mantenimiento-extintor' in request.POST:
        extintor=ActivoExtintor.objects.get(id=int(request.POST['pk_extintor']))
        form=RegistrarMantenimientoForm(request.POST, request.FILES)
        if form.is_valid():
            registro=form.save()
            print(registro)
            detalle=MantenimientoExtintor.objects.create(
                fkExtintor=extintor,
                fkRegistrarMantenimiento=RegistrarMantenimiento.objects.get(id=registro.id)
            )
            messages.success(
                request, f"SE REGISTRO EL MANTENIMIENTO DEL EXTINTOR EXITOSAMENTE"
            )
        else:
            messages.error(
                request, f"ERROR!!!, NO SE PUDO REGISTRAR EL MANTENIMIENTO DEL EXTINTOR"
            )

    # ############################################################################################################################
    # BLOQUE DE CODIGO PARA REGISTRAR MANTENIMIENTO CON EQUIPO DE OFICINA
    if request.method == "POST" and 'r-mantenimiento-equipo' in request.POST:
        equipo=ActivoEquipoOficina.objects.get(id=int(request.POST['pk_equipo']))
        form=RegistrarMantenimientoForm(request.POST, request.FILES)
        if form.is_valid():
            registro=form.save()
            print(registro)
            detalle=MantenimientoEquipo.objects.create(
                fkEquipo=equipo,
                usado=request.POST['usado'],
                fkRegistrarMantenimiento=RegistrarMantenimiento.objects.get(id=registro.id)
            )
            messages.success(
                request, f"SE REGISTRO EL MANTENIMIENTO DEL EQUIPO DE OFICINA EXITOSAMENTE"
            )
        else:
            messages.error(
                request, f"ERROR!!!, NO SE PUDO REGISTRAR EL MANTENIMIENTO DEL EQUIPO DE OFICINA"
            )
    
        # form=RegistrarMantenimientoForm()
    
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
@login_required(login_url='login')
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


# Funcion para el Logout o cierre de sesión
def logout_user(request):
    logout(request)
    return redirect("login")