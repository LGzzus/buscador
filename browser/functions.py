import ast
import os
class ResultadosClass:
    def __init__(self, url, apariciones):
        self.url = url
        self.apariciones = apariciones

def buscar_palabra(busqueda):
    current_directory = os.path.dirname(__file__)
    archivo_indice = os.path.join(current_directory, 'resultado.txt')
    try:
        with open(archivo_indice, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
        for linea in lineas:
            if busqueda + ':' in linea:
                informacion = linea.replace(busqueda + ': ', '').strip()
                try:
                    informacion = ast.literal_eval(informacion)
                    return informacion
                except (ValueError, SyntaxError):
                    return f'Error al procesar la información para la palabra "{busqueda}".'

        return f'La palabra "{busqueda}" no se encuentra en el índice invertido.'

    except FileNotFoundError:
        return f'El archivo {archivo_indice} no se encuentra.'
        
def convertir_cadena_a_objetos(cadena):
    cadena_de_texto = str(cadena)
    print(f'Contenido de cadena_de_texto: {cadena}')
    try:
        lista_tuplas = ast.literal_eval(cadena_de_texto)
        lista_objetos = [ResultadosClass(url, apariciones) for url, apariciones in lista_tuplas]
        return lista_objetos
    except (ValueError, SyntaxError) as e:
        return None
