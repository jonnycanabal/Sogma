from multiprocessing import context
from django.shortcuts import redirect, render
from activos.models import ActivoEquipoOficina, ActivoExtintor, ActivoVehiculo
from activos.forms import ActivoEquipoOficinaForm, ActivoExtintorForm, ActivoVehiculoForm

# Create your views here.

def control_activos(request):
    titulo='control-activos'
    extintores= ActivoExtintor.objects.filter(estadoExtintor="Activo")
    vehiculos=ActivoVehiculo.objects.all()
    equipos=ActivoEquipoOficina.objects.all()
    # formExtintor=ActivoExtintorForm()
    # formVehiculo=ActivoVehiculoForm()
    # formEquipoOficina=ActivoEquipoOficinaForm()
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

    if request.method == "POST" and 'c-editar-extintor' in request.POST:
        print("######################", request.POST)
        extintor = ActivoExtintor.objects.get(id=int(request.POST['pk_extintor']))
        form=ActivoExtintorForm(request.POST,instance=extintor)
        if form.is_valid():
            form.save()
        else:
          print("error editar extintor")

    if request.method == "POST" and 'form-extintor' in request.POST:
        form=ActivoExtintorForm(request.POST)
        if form.is_valid():
            form.save()
            print('###################################### EXTINTOR CREADO')
        else:
            form=ActivoExtintorForm(request.POST)
            print('###################################### EXTINTOR ERROR')

    if request.method == "POST" and 'form-oficina' in request.POST:
        form=ActivoEquipoOficinaForm(request.POST)
        if form.is_valid():
            form.save()
            print('###################################### EQUIPO CREADO')
        else:
            form=ActivoEquipoOficinaForm(request.POST)
            print('###################################### EQUIPO ERROR')

    if request.method == "POST" and 'form-vehiculo' in request.POST:
        form=ActivoVehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            print('###################################### VEHICULO CREADO')
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



# FUNCIONES PARA ELIMINAR O INHABILITAR LOS VEHICULOS
def control_activos_eliminar_vehiculo(request,pk):
    titulo = 'control-activos'
    estadoVehiculo='Activo'
    vehiculos=ActivoVehiculo.objects.all()

    # Bloque de codigo para ELIMINAR O DESACTIVAR UN ACTIVO
    ActivoVehiculo.objects.filter(id=pk).update(
        estadoVehiculo='Inactivo'
    )
    return redirect('control-activos')
    # if estadoVehiculo == 'Inactivo':
    #     return redirect('control-activos')
    # else:
    #     print('Error')

    context ={
        'titulo':titulo,
        'vehiculos':vehiculos,
    }

    return render (request, 'activos/controlActivos.html', context)


# FUNCIONES PARA ELIMINAR O INHABILITAR LOS EXTINTORES
def control_activos_eliminar_extintor(request,pk):
    # Bloque de codigo para ELIMINAR O DESACTIVAR UN ACTIVO
    ActivoExtintor.objects.filter(id=pk).update(
        estadoExtintor='Inactivo'        
    )

    return redirect('control-activos')
    

# FUNCIONES PARA ELIMINAR O INHABILITAR LOS EQUIPOS DE OFICINA
def control_activos_eliminar_equipo(request,pk):
    titulo = 'control-activos'
    equipos=ActivoEquipoOficina.objects.all()

    # Bloque de codigo para ELIMINAR O DESACTIVAR UN ACTIVO
    ActivoEquipoOficina.objects.filter(id=pk).update(
        estadoEquipo='Inactivo'
    )

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