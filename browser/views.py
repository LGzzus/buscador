from django.http import HttpResponse
from django.template import Template, Context
from browser.functions import buscar_palabra, convertir_cadena_a_objetos
import os

def principal(request): # Vista Principal
    current_directory = os.path.dirname(__file__)
    template_path = os.path.join(current_directory,'plantillas','principal.html')
    doc_palntilla_principal = open(template_path,'r')
    plt_principal = Template(doc_palntilla_principal.read())
    doc_palntilla_principal.close()
    ctx_principal = Context()
    barraBusqueda = plt_principal.render(ctx_principal)
    return HttpResponse(barraBusqueda)

def resultados(request):
    busqueda = request.GET.get('busqueda', '')
    resultado = buscar_palabra(busqueda)

    # Verificar si resultado es una cadena antes de usar startswith
    if isinstance(resultado, str) and resultado.startswith('No hay resultados'):
        # Si no hay resultados, devolver un mensaje simple.
        return HttpResponse('Ups, no hay resultados para la búsqueda: "{}"'.format(busqueda))

    lista_resultados = convertir_cadena_a_objetos(resultado)
    current_directory = os.path.dirname(__file__)
    template_path = os.path.join(current_directory,'plantillas','resultados.html')
    # Resto del código para cargar y renderizar tu plantilla
    doc_plantilla_resultados = open(template_path,'r')
    plt_resultados = Template(doc_plantilla_resultados.read())
    doc_plantilla_resultados.close()
    ctx_resultados = Context({"lista_resultados": lista_resultados, "resultado": busqueda})
    resultados = plt_resultados.render(ctx_resultados)

    return HttpResponse(resultados)