from multiprocessing import context
from django.shortcuts import render
from activos.forms import ActivoEquipoOficinaForm, ActivoExtintorForm, ActivoVehiculoForm

# Create your views here.

def control_activos(request):
    titulo='control-activos'
    form=ActivoExtintorForm()
    form2=ActivoEquipoOficinaForm()
    form3=ActivoVehiculoForm()
    context={
        'titulo':titulo,
        'form':form,
        'form2':form2,
        'form3':form3
    }
    return render (request, 'activos/controlActivos.html', context)





# def activo_extintor(request):
#     titulo='control-activos'
#     form=ActivoExtintorForm()
#     context={
#         'titulo':titulo,
#         'form':form
#     }
#     return render (request, 'gestionActivos/controlActivos.html', context)

# def activo_equipo_oficina(request):
#     titulo='control-activos'
#     form=ActivoEquipoOficinaForm()
#     context={
#         'titulo':titulo,
#         'form':form
#     }
#     return render (request, 'gestionActivos/controlActivos.html', context)

# def activo_vehiculo(request):
#     titulo='control-activos'
#     form=ActivoVehiculoForm()
#     context={
#         'titulo':titulo,
#         'form':form
#     }
#     return render (request, 'gestionActivos/controlActivos.html', context)


# ---------------------------FUNCIONES PARA CONSULTAR VEHICULOS, EXTINTOR Y EQUIPOS DE OFICINA---------------------------------