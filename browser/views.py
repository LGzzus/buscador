from django.http import HttpResponse
from django.template import Template, Context
from browser.functions import buscar_palabra, convertir_cadena_a_objetos
import os 

def principal(request):
    # Obtén el directorio del script actual
    current_directory = os.path.dirname(__file__)

    # Construye la ruta completa al archivo principal.html
    template_path = os.path.join(current_directory, 'plantillas', 'principal.html')

    try:
        # Intenta abrir el archivo
        with open(template_path, 'r') as template_file:
            # Lee el contenido del archivo
            content = template_file.read()

        # Crea un objeto de la clase Template
        plt_principal = Template(content)

        # Crea un objeto de la clase Context (puedes pasar datos si es necesario)
        ctx_principal = Context()

        # Renderiza la plantilla con el contexto
        barraBusqueda = plt_principal.render(ctx_principal)

        # Devuelve la respuesta HTTP con el contenido renderizado
        return HttpResponse(barraBusqueda)

    except FileNotFoundError:
        # Maneja el caso donde el archivo no se encuentra
        return HttpResponse("El archivo principal.html no se encuentra.")

def resultados(request):
    busqueda = request.GET.get('busqueda', '')
    resultado = buscar_palabra(busqueda)

    # Verificar si resultado es una cadena antes de usar startswith
    if isinstance(resultado, str) and resultado.startswith('No hay resultados'):
        # Si no hay resultados, devolver un mensaje simple.
        return HttpResponse('Ups, no hay resultados para la búsqueda: "{}"'.format(busqueda))

    lista_resultados = convertir_cadena_a_objetos(resultado)
    
    # Resto del código para cargar y renderizar tu plantilla
    doc_plantilla_resultados = open(r"https://github.com/LGzzus/buscador/blob/master/browser/plantillas/resultados.html")
    plt_resultados = Template(doc_plantilla_resultados.read())
    doc_plantilla_resultados.close()
    ctx_resultados = Context({"lista_resultado": lista_resultados, "resultado": busqueda})
    resultados = plt_resultados.render(ctx_resultados)

    return HttpResponse(resultados)
