from multiprocessing import context
from django.shortcuts import render,redirect
from activos.models import ActivoEquipoOficina, ActivoExtintor, ActivoVehiculo
from gestionActivos.models import GenerarRuta, MantenimientoEquipo, MantenimientoExtintor, MantenimientoVehiculo, Pasajero, RegistrarMantenimiento, DetalleRuta
from gestionActivos.forms import AlarmasForm, GenerarRutaForm, EditarGenerarRutaForm, PasajeroForm, RegistrarMantenimientoForm,DetalleRutaForm
from usuarios.models import Usuario
from django.contrib import messages
from datetime import datetime

# Importe con el cual habilitamos el @login_required
from django.contrib.auth.decorators import login_required, permission_required
# Importe para logout en la funcion logout_user
from django.contrib.auth import logout 

# Create your views here.

# ##################################################################################################################################
# FUNCION * GENERAR ALARMA *
@login_required(login_url='login')
def consultar_alarma(request):
    titulo='Alarmas'
    form=AlarmasForm()

    context={
        'titulo':titulo,
        'form':form
    }
    return render (request, 'gestionActivos/Alarmas.html', context)

# ##################################################################################################################################
# FUNCION * GENERAR RUTA *
@login_required(login_url='login')
@permission_required('gestionActivos.view_generarruta', 'gestionActivos.view_detalleruta')
def generar_ruta(request,pk=None):
    titulo='Consultar-Ruta'
    if pk==None:
        ruta=None
        detalles=None
        kilometraje= None
    else:
        ruta= GenerarRuta.objects.get(id=pk)
        usuario=Usuario.objects.get(user_id=request.user.id)

        if ruta.fkUsuario == usuario:
            detalles=DetalleRuta.objects.filter(fkRuta_id=pk)
            kilometraje=GenerarRuta.objects.filter(fkVehiculo=ruta.fkVehiculo, kilometrajeFinalVehiculo__gt=0).order_by('-fechaRegreso', '-horaRegreso')
            if kilometraje:
                kilometraje=kilometraje[0]
            else:
                kilometraje = None
        else:
            messages.warning(
                request,f"ESTA INTENTANDO INGRESAR A UNA RUTA NO ASOCIADA"
            )
            return redirect('generar-ruta')

    pasajeros= Pasajero.objects.all()
    form=None
    vehiculos=ActivoVehiculo.objects.all()
    usuarios=Usuario.objects.all()

    # ############################################################################################
    # Bloque para generar el formulario de la ruta.
    if request.method== 'POST' and 'generar' in request.POST:
        form=GenerarRutaForm(request.POST)

        if form.is_valid():
            if int(request.POST['horaSalida'][:2]) >= datetime.now().hour:
                aux=form.save()
                messages.success(
                    request,f"SE REGISTRO LA RUTA EXITOSAMENTE"
                )
                return redirect('generar-ruta',pk=aux.id)
            else:
                form=GenerarRutaForm(request.POST)
                messages.warning(
                    request,f"Error, La hora no debe ser menor a la actual"
                )
        else:
            form=GenerarRutaForm(request.POST)
            messages.error(
                request,f"Error al generar la ruta"
            )


    # ############################################################################################
    # Bloque para editar y terminar de registrar la ruta.
    if request.method == 'POST' and 'editar-ruta' in request.POST:
        ruta = GenerarRuta.objects.get(id=pk)
        
        form = EditarGenerarRutaForm(request.POST, instance=ruta)
        if form.is_valid():
            # kilometraje=GenerarRuta.objects.filter(fkVehiculo=ruta.fkVehiculo, kilometrajeFinalVehiculo__gt=0).order_by('-fechaRegreso', '-horaRegreso')[0]
            # print("#########################################", kilometraje)

            if kilometraje:
                if kilometraje.kilometrajeFinalVehiculo < int(request.POST['kilometrajeFinalVehiculo']):
                    form.save()
                    messages.success(
                        request,f"SE EDITO LA RUTA CORRECTAMENTE"
                    )

                else:
                    form=EditarGenerarRutaForm(request.POST)
                    messages.warning(
                        request,f"EL KILOMETRAJE NO PUEDE SER MENOR AL ULTIMO REGISTRADO"
                    )

            else:
                if int(request.POST['kilometrajeFinalVehiculo']) == 0:
                    messages.warning(
                        request,f"EL KILOMETRAJE NO PUEDE SER IGUAL A 0"
                    )
                else:
                    form.save()
                    messages.success(
                        request,f"SE EDITO LA RUTA CORRECTAMENTE"
                    )

            return redirect('generar-ruta',pk)

        else:
            form=EditarGenerarRutaForm(request.POST)
            messages.error(
                request,f"ERROR!!!, NO SE PUDO EDITAR LA RUTA."
            )

    # ############################################################################################
    # Bloque para agregar el pasajero a la ruta.
    if request.method== 'POST' and 'pasajero' in request.POST:
        form=DetalleRutaForm(request.POST)
        if form.is_valid():
            pasajero=DetalleRuta.objects.filter(fkRuta_id=pk, fkPasajero_id=int(request.POST["fkPasajero"]))
            if pasajero:
                messages.warning(
                request,f"EL PASAJERO YA SE ENCUENTRA AGREGADO A LA RUTA"
                )
            else:
                form.save()
                messages.success(
                    request,f"SE Agregó pasajero a LA RUTA EXITOSAMENTE"
                )
            return redirect('generar-ruta',pk)
        else:
            form=DetalleRutaForm(request.POST)
            messages.error(
                request,f"Error al agregar el pasajero a la ruta"
            )

    # ############################################################################################
    # Bloque para registrar un nuevo pasajero.
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
        'detalles':detalles,
        'titulo':titulo,
        'vehiculos':vehiculos,
        'usuarios':usuarios,
        'form':form,
        'ruta':ruta,
        'pasajeros':pasajeros,
        'kilometraje':kilometraje,
    }
    return render (request, 'gestionActivos/generarRuta.html', context)

# ############################################################################################
# Bloque para cerrar la ruta

def cerrar_ruta(request,pk):
    rutas=GenerarRuta.objects.all()
    GenerarRuta.objects.filter(id=pk).update(
        estadoRuta='Cerrada'
    )
    messages.success(
        request,f"SE CERRO LA RUTA"
        )

    return redirect('generar-ruta')

    context ={
        'rutas':rutas,
    }

    return render (request, 'gestionActivos/generarRuta.html', context)

# ####################################################################################################################
# BLOQUE PARA ELIMINAR PASAJERO
@login_required(login_url='login')
@permission_required('gestionActivos.view_pasajero')
def eliminar_pasajero(request,id):
    pasajero=DetalleRuta.objects.get(id=id)
    ruta=pasajero.fkRuta
    pasajero.delete()

    return redirect('generar-ruta', ruta.id)

# ##################################################################################################################################
# FUNCION * REGISTRAR MANTENIMIENTO *
@login_required(login_url='login')
@permission_required('gestionActivos.view_registrarmantenimiento')
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
                usado=request.POST['usado'],
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
                fkEquipoOficina=equipo,
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
@permission_required('gestionActivos.view_detalleruta')
def consultar_ruta(request):
    titulo='Consultar-Ruta'
    extintores= ActivoExtintor.objects.all()
    vehiculos=ActivoVehiculo.objects.all()
    equipos=ActivoEquipoOficina.objects.all()
    rutas=GenerarRuta.objects.all()
    vehiculo=None

    # Bloque de codigo para traer informacion de la tabla a los campos de la pagina html por medio de la Primary Key
    if request.method == "POST" and 'editar-vehiculo' in request.POST:
        vehiculo = ActivoVehiculo.objects.get(id=int(request.POST['pk_vehiculo']))

    context={
        'titulo':titulo,
        'extintores':extintores,
        'vehiculos':vehiculos,
        'vehiculo':vehiculo,
        'equipos':equipos,
        'rutas':rutas,
    }
    return render (request, 'gestionActivos/consultarRuta.html', context)


# Funcion para el Logout o cierre de sesión
def logout_user(request):
    logout(request)
    return redirect("login")