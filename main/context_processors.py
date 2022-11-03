from usuarios.models import Usuario

def sesion(request):
    usuario_actual=request.user
    image_user=r"media/usuarios/default.jpg"
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