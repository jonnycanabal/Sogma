from multiprocessing import context
from django.shortcuts import redirect, render

from usuarios.forms import UsuarioForm
from usuarios.models import Usuario


# Create your views here.

def usuarios_creados(request):
    titulo='Usuarios - Creados'
    usuarios = Usuario.objects.all()
    context={
        'titulo':titulo,
        'usuarios': usuarios
    }
    return render (request, 'usuarios/usuariosCreados.html', context)

def nuevo_usuario(request):
    titulo='Nuevo-Usuario'
    if request.method == "POST":
        print(request.POST)
        form=UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios-creados')
        else:
            form=UsuarioForm(request.POST)

    else:
        form=UsuarioForm()
    context={
        'titulo':titulo,
        'form': form
    }
    return render (request, 'usuarios/nuevoUsuario.html', context)
