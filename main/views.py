from django.shortcuts import render

# views de la pagina de Inicio - Index
def inicio (request):

    titulo = 'Index'
    context = {
        'titulo': titulo
    }

    return render (request, 'index.html', context)

# views de la pagina de Control Activos
def control_activos (request):

    titulo = 'Control-Activos'
    context = {
        'titulo': titulo
    }

    return render (request,'controlActivos.html', context)

# views de la pagina Generar Alarma
def generar_alarma (request):

    titulo = 'Generar-Alarma'
    context = {
        'titulo': titulo
    }

    return render (request, 'generarAlarma.html', context)

# views de la pagina de Generar Ruta
def generar_ruta (request):

    titulo = 'Generar-Ruta'
    context = {
        'titulo': titulo
    }

    return render (request, 'generarRuta.html', context)

# views de la pagina de Consultar Ruta
def consultar_ruta (request):

    titulo = 'Consultar-Ruta'
    context = {
        'titulo': titulo
    }

    return render (request, 'consultarRuta.html', context)

# views de la pagina de Nuevo Usuario
def nuevo_usuario (request):

    titulo = 'Nuevo-Usuario'
    context = {
        'titulo': titulo
    }

    return render (request, 'nuevoUsuario.html')

# views de la pagina de Registrar Mantenimiento
def registrar_mantenimiento (request):

    titulo = 'Registrar-Mantenimiento'
    context = {
        'titulo': titulo
    }

    return render (request, 'registrarMantenimiento.html', context)