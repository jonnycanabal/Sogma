from usuarios.models import Usuario
from gestionActivos.models import MantenimientoVehiculo, MantenimientoExtintor, MantenimientoEquipo
from datetime import datetime, timedelta


def sesion(request):
    usuario_actual=request.user
    image_user=r"media/usuarios/default.png"
    usuario=None
    if request.user.is_authenticated:
        if Usuario.objects.filter(user_id=usuario_actual.id):
            image_user=Usuario.objects.get(user_id=usuario_actual.id).foto.url
            usuario=Usuario.objects.get(user_id=usuario_actual.id)
    context={
        'usuario_actual':usuario_actual,
        'image_user':image_user,
        'usuario':usuario
    }

    return context

# Bloque de código con la función para dar aviso de activos que esten proximos a un mantenimiento.
def alarma (request):
    start_date_vehiculo= datetime.today() - timedelta(days=365)
    end_date_vehiculo= datetime.today() + timedelta(days=3) - timedelta(days=300)

    start_date_extintor= datetime.today() - timedelta(days=395)
    end_date_extintor= datetime.today() + timedelta(days=30) - timedelta(days=365)

    start_date_equipo= datetime.today() - timedelta(days=395)
    end_date_equipo= datetime.today() + timedelta(days=30) - timedelta(days=365)
    # vehiculos=MantenimientoVehiculo.objects.filter(fkRegistrarMantenimiento__fechaMantenimiento__range=(start_date, end_date))
    vehiculos=MantenimientoVehiculo.objects.filter(fkRegistrarMantenimiento__fechaMantenimiento__gte= start_date_vehiculo, fkRegistrarMantenimiento__fechaMantenimiento__lte= end_date_vehiculo)
    extintores=MantenimientoExtintor.objects.filter(fkRegistrarMantenimiento__fechaMantenimiento__gte= start_date_extintor, fkRegistrarMantenimiento__fechaMantenimiento__lte= end_date_extintor)
    equipos=MantenimientoEquipo.objects.filter(fkRegistrarMantenimiento__fechaMantenimiento__gte= start_date_equipo, fkRegistrarMantenimiento__fechaMantenimiento__lte= end_date_equipo)

    # for vehiculo in vehiculos:
    #     print(vehiculos)

    # for extintor in extintores:
    #     print(extintores)

    # for equipo in equipos:
    #     print(equipos)

    context={
        'vehiculos':vehiculos,
        'extintores':extintores,
        'equipos':equipos
    }
    return context