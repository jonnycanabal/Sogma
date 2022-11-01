from usuarios.models import Usuario

def sesion(request):
    usuario_actual=request.user
    image_user=r"../media/usuarios/default.jpg" # VERFICIAR SI ES CON R O F ESTA LINEA DE CODIGO -----------------
    if request.user.is_authenticated:
        if Usuario.objects.filter(user_id=usuario_actual.id):
            image_user=Usuario.objects.get(user_id=usuario_actual.id).foto.url
    context={
        'usuario_actual':usuario_actual,
        'image_user':image_user
    }

    return context