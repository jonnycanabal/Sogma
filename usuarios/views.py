from multiprocessing import context
from django.shortcuts import redirect, render

from usuarios.forms import UsuarioForm, UsuarioEditarForm
from usuarios.models import Usuario
from django.contrib import messages


from django.contrib.auth.models import User, Group
# Importe para logout en la funcion logout_user
from django.contrib.auth import logout 

# Importe con el cual habilitamos la función de make_password en nuestra contraseña que se crea por defecto.
from django.contrib.auth.hashers import make_password
# Importe con el cual habilitamos el @login_required
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
# @login_required pequeño fragmento de codigo con el cual hacemos necesario un inicio de sesion para ingresar a esta función y/o
# página a la cual este asociada
@login_required(login_url='login')
@permission_required('usuarios.view_usuario')
def usuarios_creados(request):
    titulo='Usuarios - Creados'
    usuarios = Usuario.objects.all()
    usuarios= Usuario.objects.filter()
    usuario=None

    # ###################################################################################################################################
    # SIRVE PARA VISUALIAR Y TRAER LA INFORMACION DE LA TABLA A LOS CAMPOS O INPUTS ESTABLECIDOS
    if request.method == "POST" and 'editar-usuario' in request.POST:
        usuario = Usuario.objects.get(id=int(request.POST['pk_usuario']))
    

    # ###################################################################################################################################
    # EDITAR USUARIO
    if request.method == "POST" and 'c-editar-usuario' in request.POST:
        print("######################", request.POST)
        usuario = Usuario.objects.get(id=int(request.POST['pk_usuario']))
        user=User.objects.get(username=usuario.numeroDocumento)
        form=UsuarioEditarForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            user.email=request.POST['correoElectronico']
            user.first_name=request.POST['primerNombre'].capitalize()
            user.last_name=request.POST['primerApellido'].capitalize()
            user.save()
            my_group= Group.objects.get(name=request.POST['tipoUsuario'])
            usuario.user.groups.clear()
            my_group.user_set.add(usuario.user)

            messages.success(
                request,f"SE EDITÓ EL USUARIO CON ID # {usuario.id} EXITOSAMENTE"
            )
        else:
            messages.error(
                request,f"ERROR NO SE EDITÓ EL USUARIO CON ID # {usuario.id} "
            )

    # ###################################################################################################################################
    # REGISTRAR USUARIO
    if request.method == "POST" and 'form-nuevo-usuario' in request.POST:
        print(request.POST)
        form=UsuarioForm(request.POST, request.FILES) # ,request.FILES -------------------------------------
        if form.is_valid():
            # ###############################################################################################################
            # Bloque de codigo para el registro del usuario y contraseña
            if not User.objects.filter(username=request.POST['numeroDocumento']):
                user = User.objects.create_user('nombre', 'email@email', 'pass')
                user.username=request.POST['numeroDocumento']
                user.first_name=request.POST['primerNombre'].capitalize()
                user.last_name=request.POST['primerApellido'].capitalize()
                user.email=request.POST['correoElectronico']
                user.password=make_password("@" + request.POST['primerNombre'][0] + request.POST['primerApellido'][0] + "." + request.POST['numeroDocumento'][-4:])
                user.save()
                # user_group= User
            else:
                user=User.objects.get(username=request.POST['numeroDocumento'])
            usuario= Usuario.objects.create(
                primerNombre=request.POST['primerNombre'],
                segundoNombre=request.POST['segundoNombre'],
                primerApellido=request.POST['primerApellido'],
                segundoApellido=request.POST['segundoApellido'],
                foto=form.cleaned_data.get('foto'),
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
            my_group= Group.objects.get(name=request.POST['tipoUsuario'])
            usuario.user.groups.clear()
            my_group.user_set.add(usuario.user)

            messages.success(
            request,f"SE REGISTRÓ EL USUARIO EXITOSAMENTE"
            )
            return redirect ('gestion-usuarios')

        else:
            form=UsuarioForm(request.POST, request.FILES) #, request.FILES

            print('######################################', form.errors)
            messages.error(
            request,f"NO SE PUDO REGISTRAR EL USUARIO. ASEGURECE DE DIGITAR CORRECTAMENTE LOS CAMPOS Y QUE ESTOS NO CONTENGAN SOLO ESPACIOS EN BLANCO"
            )
    else:
        form=UsuarioForm()


    context={
        'titulo':titulo,
        'usuarios': usuarios,
        'usuario':usuario,
        'form':form,
    }
    return render (request, 'usuarios/gestionUsuarios.html', context)

# ###################################################################################################################################
# ELIMINAR O DESABILITAR USUARIO
@login_required(login_url='login')
@permission_required('usuarios.view_usuario')
def eliminar_usuario(request,pk):
    titulo = 'Usuarios'
    usuarios=Usuario.objects.all()

    # Bloque de codigo para ELIMINAR O DESACTIVAR UN USUARIO
    Usuario.objects.filter(id=pk).update(
        estado='0'
    )
    messages.success(
            request,f"SE INACTIVÓ EL USUARIO EXITOSAMENTE"
        )

    return redirect('gestion-usuarios')

    context ={
        'titulo':titulo,
        'usuarios':usuarios,
    }

    return render (request, 'usuarios/usuariosCreados.html', context)



# ###########################################################################################################################
# Funcion para el Logout o cierre de sesión
def logout_user(request):
    logout(request)
    return redirect("login")