
from email.mime import image

# from usuarios.models import Usuario

# def sesion(request):
#     usuario_actual=request.user
#     image_user=None
#     if request.user.is_authenticated:
#         image_user=Usuario.objects.get(user_id=current_user.id).foto.url
#     context={
#         'usuario_actual':usuario_actual,
#         'image_user':image_user
#     }

#     return context