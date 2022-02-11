
# Importar Aemet
from aemet import Aemet

# Aemet Key
key = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhamltZW5lemFkYWxpYUBnbWFpbC5jb20iLCJqdGkiOiJlYjRhNDBmOS0xYTZhLTQ1YzgtYTk3My0wNmUwZGNjMDU0NzUiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTY0MzI4Nzg0OSwidXNlcklkIjoiZWI0YTQwZjktMWE2YS00NWM4LWE5NzMtMDZlMGRjYzA1NDc1Iiwicm9sZSI6IiJ9.ptBTeYQdnaA9ZnnrgAkB1JeTz0PNOJCP5CIXXeZ1iTU'

aemet_client = Aemet(api_key=key)


##### Ejercicio 3.
# Descargar un mapa con las borrascas y anticiclones
aemet_client.descargar_mapa_analisis("mapa_analisis.jpg")

# Mostrar el mapa
from PIL import Image

mapa_borrascas = Image.open("mapa_analisis.jpg")
mapa_borrascas.show()

##### Ejercicio 4.
# Descargar un mapa de rayos
aemet_client.descargar_mapa_rayos("mapa_rayos.jpg")

# Mostrar el mapa
mapa_rayos = Image.open("mapa_rayos.jpg")
mapa_rayos.show()

##### Ejercicio 5.
# Descargar un mapa con el riesgo de incendio estimado en Canarias
aemet_client.descargar_mapa_riesgo_estimado_incendio(
    "mapa_incendio_canarias.jpg", area='c')

# Mostrar el mapa
mapa_incendio_canarias = Image.open("mapa_incendio_canarias.jpg")
mapa_incendio_canarias.show()

##### Ejercicio 6. (STATUS 404)
# Obtener un mapa con el Indice de Vegetación de Diferencia Normalizada.
aemet_client.descargar_mapa_satelite_nvdi("mapa_nvdi.jpg")

# Mostrar el mapa
mapa_nvdi = Image.open("mapa_nvdi.jpg")
mapa_nvdi.show()

##### Ejercicio 7.
# Obtener la predicción del tiempo en España (método get_prediccion_normalizada)
prediccion = aemet_client.get_prediccion_normalizada()
print(prediccion)

##### Ejercicio 8.
# Predicción meteorológica para la CAM
prediccion_madrid = aemet_client.get_prediccion_normalizada(
    ambito='ccaa', ccaa='mad')
print(prediccion_madrid)

