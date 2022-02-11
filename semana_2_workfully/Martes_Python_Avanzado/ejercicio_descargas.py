


'''
1. Crear directorios en la carpeta Descargas:
- Image
- Documents
- Software
- Others

2. Al ejecutar el script, se mueven automáticamente los archivos al
directorio correspondiente, dependiendo de su extensión.
'''

import os
import shutil


directorio_raiz = os.getcwd()

class Limpiador:
    """Automatiza la limpieza de un directorio
    """
    def __init__(self, ruta_carpeta):
        """Constructor de la clase Limpiador.

        Params:
            - ruta_carpeta: str, ruta absoluta de la carpeta a limpiar
        """
        self.ruta_carpeta = ruta_carpeta
        # Movimiento hacia la carpeta recibida por parámetro
        if os.path.exists(self.ruta_carpeta):
            os.chdir(self.ruta_carpeta)
        else:
            self.path_error(self.ruta_carpeta)

    def path_error(self, ruta_no_valida):
        """Devuelve un error de pathing
        """
        return f"Error. No se encontró la ruta {ruta_no_valida}."

    def limpiar(self):
        """Mueve los archivos a directorios pre-establecidos, dentro de la
        carpeta recibida en el constructor.
        """
        # Creando carpetas (si no existen)
        carpetas = ['Image', 'Documents', 'Software', 'Others']
        for carpeta in carpetas:
            try:
                os.mkdir(carpeta)
            except FileExistsError:
                continue

        # Extensiones de archivos (por tipo)
        imagenes = ['.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff']
        documentos = ['.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx']
        software = ['.exe', '.pkg', '.dmg']

        for archivo in os.listdir():
            cuatro_ultimos = archivo[-5:]
            tres_ultimos = archivo[-4:]

            if cuatro_ultimos in imagenes or tres_ultimos in imagenes:
                shutil.move(archivo, 'Image/')
            elif cuatro_ultimos in documentos or tres_ultimos in documentos:
                shutil.move(archivo, 'Documents/')
            elif tres_ultimos in software:
                shutil.move(archivo, 'Software/')
            else:
                if '.' in archivo:
                    shutil.move(archivo, 'Others/')

        print('Limpieza finalizada.')



# Si el usuario no soy yo, le preguntamos su ruta
try:
    directorio_descargas = '/Users/antoniojimenez/Downloads'
    os.chdir(directorio_descargas)

    # Creamos un objeto de tipo Limpiador
    cleaner = Limpiador(directorio_descargas)
    # Ejecutamos la limpieza
    cleaner.limpiar()

except FileNotFoundError:
    ruta_usuario = input('Introduce la ruta de la carpeta a limpiar: ')

    # Creamos un objeto de tipo Limpiador
    cleaner = Limpiador(ruta_usuario)
    # Ejecutamos la limpieza
    cleaner.limpiar()

finally:
    # Volvemos a nuestro directorio inicial de trabajo
    os.chdir(directorio_raiz)
    print('Directorio raíz re-establecido.')