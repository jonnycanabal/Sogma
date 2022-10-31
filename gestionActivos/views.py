from multiprocessing import context
from django.shortcuts import render,redirect
from activos.models import ActivoEquipoOficina, ActivoExtintor, ActivoVehiculo
<<<<<<< Updated upstream
from gestionActivos.models import GenerarRuta, Pasajero
from gestionActivos.forms import GenerarAlarmaForm, GenerarRutaForm, PasajeroForm, RegistrarMantenimientoForm
from usuarios.models import Usuario
from django.contrib import messages

# Importe con el cual habilitamos el @login_required
from django.contrib.auth.decorators import login_required
# Importe para logout en la funcion logout_user
from django.contrib.auth import logout 

=======
from gestionActivos.models import GenerarRuta
from gestionActivos.forms import GenerarAlarmaForm, GenerarRutaForm, RegistrarMantenimientoForm
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
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
=======
    vehiculos=ActivoVehiculo.objects.all()
    form=GenerarRutaForm()
    if request.method== 'POST':
        
        return redirect('agregar-ruta', 1)
>>>>>>> Stashed changes

    

    context={
        'titulo':titulo,
        'vehiculos':vehiculos,
<<<<<<< Updated upstream
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
=======
        'form':form,
        'ruta':ruta
    }
    return render (request, 'gestionActivos/generarRuta.html', context)

>>>>>>> Stashed changes
def agregar_funcionarios_ruta(request, pk):
    titulo='Consultar-Ruta'
    ruta= GenerarRuta.objects.get(id=pk)
    # pasajeros= DetalleRuta.objects.filter(fkRuta_id=pk)

    context={
        'titulo':titulo,
<<<<<<< Updated upstream
        # 'vehiculos':vehiculos,
=======
        'vehiculos':vehiculos,
>>>>>>> Stashed changes
        'ruta':ruta
    }
    return render (request, 'gestionActivos/generarRuta.html', context)

<<<<<<< Updated upstream
# def eliminar_pasajero(request):

#     context={

#     }

#     return render (request, 'gestionActivos/generarRuta.html', context)

# ##################################################################################################################################
# FUNCION * REGISTRAR MANTENIMIENTO *
@login_required(login_url='login')
=======

>>>>>>> Stashed changes
def registrar_mantenimiento(request):
    titulo='Registrar-Mantenimiento'
    extintores= ActivoExtintor.objects.all()
    vehiculos=ActivoVehiculo.objects.all()
    equipos=ActivoEquipoOficina.objects.all()
    extintor=None
    vehiculo=None
    equipo=None

    # ####################################################################################################################
    # Bloque de codigo para traer informacion de la tabla a los campos de la pagina html por medio de la Primary Key
    if request.method == "POST" and 'editar-extintor' in request.POST:
        extintor = ActivoExtintor.objects.get(id=int(request.POST['pk_extintor']))

    if request.method == "POST" and 'editar-vehiculo' in request.POST:
        vehiculo = ActivoVehiculo.objects.get(id=int(request.POST['pk_vehiculo']))

    if request.method == "POST" and 'editar-equipo-oficina' in request.POST:
        equipo = ActivoEquipoOficina.objects.get(id=int(request.POST['pk_equipo']))

    # ####################################################################################################################
    if request.method == "POST":
        form=RegistrarMantenimientoForm(request.POST)
        if form.is_valid():
            form.saved()
            print('###################################### MANTENIMIENTO REGISTRADO')
            messages.success(
                request, f"EL MANTENIMIENTO SE REGISTRO DE FORMA EXITOSA"
            )

            return redirect('registrar-mantenimiento')
        else:
            form=RegistrarMantenimientoForm(request.POST)
            print('###################################### ERROR MANTENIMIENTO NO REGISTRADO')
            messages.error(
                request, f"ERROR, EL MANTENIMIENTO NO SE PUDO REGISTRAR!!!!!!!"
            )
    
    else:
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