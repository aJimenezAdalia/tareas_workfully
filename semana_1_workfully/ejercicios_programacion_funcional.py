

##### Ejercicio 1.
# Utiliza reduce para concatenar estas palabras en una frase
ejer_1 = ("to", "be", "or", "not", "to", "be", "that", "is", "the", "question")
from functools import reduce
reduce_1 = reduce(lambda x,y: x + ' ' + y, ejer_1)

##### Ejercicio 2.
# Obtén una nueva tupla con el cuadrado de cada elemento
ejer_2 = (1,2,3,4,5)

map_2 = list(map(lambda x: x**2, ejer_2))

##### Ejercicio 3.
# Filtra aquellos elementos que sean multiplos de 3 o de 5
ejer_3 = (1,2,3,4,5,15,21,22,33,34,35)

def mult_3_5(x):
    if x % 3 == 0 or x % 5 == 0:
        return True
    return False

filtrado = list(filter(mult_3_5, ejer_3))

##### Ejercicio 4.
# Convierte la siguiente tupla de pesetas a euros
ejer_4 = (1000, 8000, 20000000, 40000000)
euros = list(map(lambda x: x/166, ejer_4))

##### Ejercicio 5.
# Convierte la siguiente lista de desconocidos a mayusculas
ejer_5 = ("Arya", "John", "Robb", "Bran", "Sansa", "Rickon")
mayus = list(map(lambda x: x.upper(), ejer_5))

##### Ejercicio 6.
# Realiza un conversor de días de la semana en texto
# a numérico (1-7) usando map
ejer_6 = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
semana = list(map(lambda x: ejer_6.index(x)+1, ejer_6))

##### Ejercicio 7.
# Utiliza map para multiplicar elemento a elemento estas dos tuplas
ejer_7_1 = (2, 5, 8)
ejer_7_2 = (6, 3, 2)

mult = list(map(lambda x,y: x*y, ejer_7_1, ejer_7_2))

##### Ejercicio 8.
# Crea una nueva tupla con todos los coches que no sean VW
ejer_8 = ("VW", "Audi", "Renault", "VW", "BMW")
no_vw = list(filter(lambda x: x != "VW", ejer_8))

##### Ejercicio 9.
# Dadas las siguientes fechas en formato string,
# quedate con aquellas del año 2020
ejer_9 = ("2019-04-08", "2020-10-10", "2020-01-22", "2019-07-13", "2019-02-01")
dosmilveinte = list(filter(lambda x: x.startswith("2020"), ejer_9))

##### Ejercicio 10.
# Filtra aquellos strings que sean palíndromos
ejer_10 = ("php", "w3r", "Python", "abcd", "Java", "aaa")
pal = list(filter(lambda x: x == x.reverse(), ejer_10))

