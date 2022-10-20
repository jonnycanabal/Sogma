from multiprocessing import context
from django.shortcuts import render
from activos.models import ActivoEquipoOficina, ActivoExtintor, ActivoVehiculo
from activos.forms import ActivoEquipoOficinaForm, ActivoExtintorForm, ActivoVehiculoForm

# Create your views here.

def control_activos(request):
    titulo='control-activos'
    extintores= ActivoExtintor.objects.all()
    vehiculos=ActivoVehiculo.objects.all()
    equipos=ActivoEquipoOficina.objects.all()
    formExtintor=ActivoExtintorForm()
    formVehiculo=ActivoVehiculoForm()
    formEquipoOficina=ActivoEquipoOficinaForm()
    extintor=None

    if request.method == "POST" and 'editar-extintor' in request.POST:
        extintor= ActivoExtintor.objects.get(id=int(request.POST['pk_extintor']))

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
        'equipos':equipos,
 
    }
    return render (request, 'activos/controlActivos.html', context)


# NO SE POR QUE REQUEIRE DE LOS DOS CODIGOS PARA GUARDAR INFORMACIÓN


# def crear_extintor(request):
#     titulo='crear-extintor'
#     if request.method == "POST":
#         form=ActivoExtintorForm(request.POST)
#         if form.is_valid():
#             form.save()
#         else:
#             form=ActivoExtintorForm(request.POST)
#     else:
#         form=ActivoExtintorForm(request.POST)
#     context={
#         'titulo':titulo,
#         'form':form
#     }
#     return render (request, 'activos/controlActivos.html', context)


# def crear_vehiculo(request):
#     titulo='control-activos'
#     if request.method == "POST":
#         form=ActivoVehiculoForm(request.POST)
#         if form.is_valid():
#             form.save()
#         else:
#             form=ActivoVehiculoForm(request.POST)
#     else:
#         form=ActivoVehiculoForm(request.POST)
#     context={
#         'titulo':titulo,
#         'form':form
#     }
#     return render (request, 'activos/controlActivos.html', context)


# def crear_equipo_oficina(request):
#     titulo='control-activos'
#     if request.method == "POST":
#         form=ActivoEquipoOficinaForm(request.POST)
#         if form.is_valid():
#             form.save()
#         else:
#             form=ActivoEquipoOficinaForm(request.POST)
#     else:
#         form=ActivoEquipoOficinaForm(request.POST)
#     context={
#         'titulo':titulo,
#         'form':form
#     }
#     return render (request, 'activos/controlActivos.html', context)


# ---------------------------FUNCIONES PARA CONSULTAR VEHICULOS, EXTINTOR Y EQUIPOS DE OFICINA---------------------------------