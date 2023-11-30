from django.http import HttpResponse
from django.template import Template, Context
from browser.functions import buscar_palabra, convertir_cadena_a_objetos
import os 

def principal(request):
    current_directory = os.path.dirname(__file__)
    template_path = os.path.join(current_directory, 'plantillas', 'principal.html')

    try:
        with open(template_path, 'r') as template_file:
            content = template_file.read()
        plt_principal = Template(content)
        ctx_principal = Context()
        barraBusqueda = plt_principal.render(ctx_principal)
        return HttpResponse(barraBusqueda)

    except FileNotFoundError:
        return HttpResponse("El archivo principal.html no se encuentra.")

def resultados(request):
    busqueda = request.GET.get('busqueda', '')
    resultado = buscar_palabra(busqueda)
    if isinstance(resultado, str) and resultado.startswith('No hay resultados'):
        return HttpResponse('Ups, no hay resultados para la búsqueda: "{}"'.format(busqueda))

    lista_resultados = convertir_cadena_a_objetos(resultado)
    current_directory = os.path.dirname(__file__)
    template_path = os.path.join(current_directory, 'plantillas', 'resultados.html')

    try:
        with open(template_path, 'r') as template_file:
            content = template_file.read()
        plt_resultados = Template(content)
        ctx_resultados = Context({"lista_resultado": lista_resultados, "resultado": busqueda})
        resultados = plt_resultados.render(ctx_resultados)
        return HttpResponse(resultados)

    except FileNotFoundError:
        return HttpResponse("El archivo resultados.html no se encuentra.")
