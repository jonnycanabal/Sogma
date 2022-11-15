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


def alarma (request):
    start_date= datetime.today() - timedelta(days=32)
    end_date= datetime.today() + timedelta(days=3) - timedelta(days=30)
    # vehiculos=MantenimientoVehiculo.objects.filter(fkRegistrarMantenimiento__fechaMantenimiento__range=(start_date, end_date))
    vehiculos=MantenimientoVehiculo.objects.filter(fkRegistrarMantenimiento__fechaMantenimiento__gte= start_date, fkRegistrarMantenimiento__fechaMantenimiento__lte= end_date)
    extintores=MantenimientoExtintor.objects.filter(fkRegistrarMantenimiento__fechaMantenimiento__gte= start_date, fkRegistrarMantenimiento__fechaMantenimiento__lte= end_date)
    equipos=MantenimientoEquipo.objects.filter(fkRegistrarMantenimiento__fechaMantenimiento__gte= start_date, fkRegistrarMantenimiento__fechaMantenimiento__lte= end_date)

    for vehiculo in vehiculos:
        print(vehiculos)

    for extintor in extintores:
        print(extintores)

    for equipo in equipos:
        print(equipos)

    context={
        'vehiculos':vehiculos,
        'extintores':extintores,
        'equipos':equipos
    }
    return context