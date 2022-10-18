from multiprocessing import context
from django.shortcuts import render

from usuarios.forms import UsuarioForm


# Create your views here.

def usuarios_crear(request):
    titulo='Usuarios - crear'
    form=UsuarioForm()
    context={
        'titulo':titulo,
        'form':form
    }
    return render (request, 'usuarios/usuarios-crear.html', context)

def nuevo_usuario(request):
    titulo='Nuevo-Usuario'
    form=UsuarioForm()
    context={
        'titulo':titulo,
        'form':form
    }
    return render (request, 'usuarios/nuevoUsuario.html', context)