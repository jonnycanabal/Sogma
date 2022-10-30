from multiprocessing import context
from django.shortcuts import redirect, render

from usuarios.forms import UsuarioForm
from usuarios.models import Usuario
from django.contrib import messages


from django.contrib.auth.models import User
# Importe para logout en la funcion logout_user
from django.contrib.auth import logout 

# Importe con el cual habilitamos la función de make_password en nuestra contraseña que se crea por defecto.
from django.contrib.auth.hashers import make_password
# Importe con el cual habilitamos el @login_required
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required pequeño fragmento de codigo con el cual hacemos necesario un inicio de sesion para ingresar a esta función y/o
# página a la cual este asociada
@login_required(login_url='login')
def usuarios_creados(request):
    titulo='Usuarios - Creados'
    usuarios = Usuario.objects.all()
    context={
        'titulo':titulo,
        'usuarios': usuarios
    }
    return render (request, 'usuarios/usuariosCreados.html', context)

@login_required(login_url='login')
def nuevo_usuario(request):
    titulo='Nuevo-Usuario'
    if request.method == "POST":
        print(request.POST)
        form=UsuarioForm(request.POST) # ,request.FILES -------------------------------------
        if form.is_valid():
            # ###############################################################################################################
            # Bloque de codigo para el registro del usuario y contraseña
            if not User.objects.filter(username=request.POST['numeroDocumento']):
                user = User.objects.create_user('nombre', 'email@email', 'pass')
                user.username=request.POST['numeroDocumento']
                user.first_name=request.POST['primerNombre'].capitalize()
                user.last_name=request.POST['primerApellido'].capitalize()
                user.email=request.POST['correoElectronico']
                user.password=make_password("@" + request.POST['primerNombre'][0] + request.POST['primerApellido'][0] + request.POST['numeroDocumento'][-4:])
                user.save()
            else:
                user=User.objects.get(username=request.POST['numeroDocumento'])
            usuario= Usuario.objects.create(
                primerNombre=request.POST['primerNombre'],
                segundoNombre=request.POST['segundoNombre'],
                primerApellido=request.POST['primerApellido'],
                segundoApellido=request.POST['segundoApellido'],
                # foto=form.cleaned_data.get('foto'),
                correoElectronico=request.POST['correoElectronico'],
                tipoDocumento=request.POST['tipoDocumento'],
                numeroDocumento=request.POST['numeroDocumento'],
                numeroTelefono=request.POST['numeroTelefono'],
                ciudadResidencia=request.POST['ciudadResidencia'],
                direccionResidencia=request.POST['direccionResidencia'],
                genero=request.POST['genero'],
                cargo=request.POST['cargo'],
                fechaRegistro=request.POST['fechaRegistro'],
            # empresa=Empresa.objects.get(id=int(request.POST['empresa'])),
                user=user,
                tipoUsuario=request.POST['tipoUsuario'],
            )

            messages.success(
            request,f"SE REGISTRO EL USUARIO EXITOSAMENTE"
            )
            return redirect ('usuarios-creados')

        else:
            form=UsuarioForm(request.POST) #, request.FILES

            print('###################################### ERROR')
            messages.error(
            request,f"NO SE REGISTRO EL USUARIO"
            )
    else:
        form=UsuarioForm()
    context={
        'titulo':titulo,
        'form': form
    }
    return render (request, 'usuarios/nuevoUsuario.html', context)

# ###########################################################################################################################
# Funcion para el Logout o cierre de sesión
def logout_user(request):
    logout(request)
    return redirect("login")