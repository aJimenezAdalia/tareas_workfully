


##### Ejercicio 1.
# Declara una variable numérica que será una hora cualquiera del día.
# Implementa mediante sentencias if/elif/else la siguiente casuística:
# - Si es entre las 0 y las 8, print "Durmiendo"
# - Si es entre las 9 y las 18, print "Trabajando"
# - Si es entre las 19 y las 21, print "Clase"
# - Si es entre las 22 y las 24, print "Descanso"
# - En cualquier otro caso, print "Transporte o error"

variable_numerica = 15

if 0 < variable_numerica < 8:
    print("Durmiendo")
elif 9 < variable_numerica < 18:
    print("Trabajando")
elif 19 < variable_numerica < 21:
    print("Clase")
elif 22 < variable_numerica < 24:
    print("Descanso")
else:
    print("Transporte o Error")


##### Ejercicio 2.
# Calculador de precios de casas. Tenemos las siguientes variables:
superficie = None
distrito = None

# Implementar mediante if/elif/else:
# 1. Si el distrito es "Moncloa" o "Centro", y además la superficie es superior a
# 100 metros cuadrados, el precio de la casa es de 1000
# 2. Si el distrito es "Salamanca", y además la superficie de la casa es al menos de
# 150 metros, el precio de la casa es de 1500
# 3. Si el distrito no es "Retiro" y la superficie está entre 60 y 80 metros, el precio es de 600
# 4. En cualquier otro caso, el precio será de 0

import random

superficie = random.randint(40, 300)
distrito = random.choice(['Moncloa', 'Centro', 'Salamanca', 'Retiro'])

if distrito in ['Moncloa', 'Centro'] and superficie > 100:
    precio = 1000
elif distrito == 'Salamanca' and superficie >= 150:
    precio = 1500
elif distrito != 'Retiro' and 60 <= superficie <= 80:
    precio = 600
else:
    precio = 0


##### Ejercicio 3.
# En este ejercicio vamos a realizar un programa muy parecido.
# Para este caso queremos que se cumplan las siguientes condiciones:
# 1. Primero se compruebe si el distrito es "Retiro". Si es asi, que imprima "Distrito Retiro",
# y si no, "Otro distrito"
# 2. Si el distrito es "Retiro", comprueba si la superficie es mayor de 100 metros cuadrados.
# En tal caso, que imprima un precio de 1000, y si no, de 500.
# Hay que usar ifs anidados

superficie = random.randint(40, 300)
distrito = random.choice(['Moncloa', 'Centro', 'Salamanca', 'Retiro'])

if distrito == 'Retiro':
    print('Distrito Retiro')
    if superficie > 100:
        print('El precio es de 1000')
    else:
        print('El precio es de 500')
else:
    print('Otro distrito')


##### Ejercicio 4.
# Escribe un programa que tenga dos variables: un numero, y una lista numérica.
# El programa debe recorrer la lista e imprimir por pantalla cada elemento de la lista
# multiplicado por el número

def multip_elemento(numero, lista):
    """Recibe un número y una lista numérica, recorre
    la lista e imprime cada elemento de la misma multiplicado
    por el número (primer argumento).

    Params:
        - numero: int
        - lista: list
    """
    # Comprobamos si el primer argumento es en realidad un número
    if not isinstance(numero, (int, float)):
        return print("Error. El número debe ser un entero o un decimal.")
    # Comprobamos si cada elemento de la lista es numérico
    for elemento in lista:
        if not isinstance(elemento, (int, float)):
            return print("Error. Los elementos de la lista deben ser todos numéricos")
    # Si seguimos aquí, es que los argumentos son correctos.
    # Imprimimos los resultados
    for elemento in lista:
        print(numero * elemento)

##### Ejercicio 5.
# Imprime por pantalla los números -10 al -1. En ese orden. Consulta la
# documentación de range

for i in range(-10,0):
    print(i)

##### Ejercicio 6.
# Dada la siguiente lista:
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

# Implementa un programa que los recorra e imprima por pantalla todos los divisibles por 5.
# Si nos encontramos con alguno que sea mayor de 150, detener el bucle.

def recorre_lista(lista):
    """Recibe una lista numérica, e imprime por pantalla
    todos los números de la misma que sean divisibles entre 5.
    Si encuentra un número mayor que 150, detiene el bucle.

    Params:
        - lista: list
    """

    # Comprobamos si todos los elementos de la lista son numéricos
    for elemento in lista:
        if not isinstance(elemento, (int, float)):
            return print("Error, los elementos de la lista deben ser numéricos.")
    # Recorremos la lista
    for elemento in lista:
        if elemento > 150:
            break
        elif elemento % 5 == 0:
            print(elemento)

##### Ejercicio 7.
# Escribe un programa en Python que imprima por pantalla todos los números divisibles
# por 5 y divisibles por 7, dentro del rango de valores (150, 350)

for i in range(150, 351):
    if i % 5 == 0 and i % 7 == 0:
        print(i)


##### Ejercicio 8.
# Implementa un programa que imprima por pantalla el siguiente patrón
'''
5 4 3 2 1
4 3 2 1 
3 2 1 
2 1 
1
'''
# NOTA: no hay líneas en blanco entre una línea y otra

# SOLUCIÓN:

'''Al parecer, sí hay líneas en blanco entre cada número, por tanto 
vamos a hacerlo así.'''


lista_nums_strings = []

nums = list(range(5,0,-1))

for i in nums:
    lista_nums_strings.append(str(i)) # Llenamos la lista vacía de los números como strings

threshold = 5

while threshold > 0:
    print(" ".join(lista_nums_strings))
    lista_nums_strings = lista_nums_strings[1:]
    threshold -= 1

##### Ejercicio 9.
# En este ejercicio vamos a crear un pequeño juego. Se trata de intentar adivinar un
# numero del 1 al 5. Tenemos dos intentos para acertar. Pasos a seguir:
# 1. Ya viene implementado cómo obtener un número aleatorio del 1 al 5
# 2. Tendrás que declarar en una variable el numero de vidas, y mediante un bucle while,
# comprobar que todavia quedan vidas.
# 3. Dentro del bucle, obtener el valor del usuario y comprobar si es ese el numero a adivinar.
# Si no, actualizar las vidas.
# 4. Si acertamos, salimos del bucle e imprimimos por pantalla "You win".
# Y si perdemos también salimos del bucle, pero en este caso imprimimos por pantalla "You lose".
# TIP: te puede resultar útil usar la sentencia else cuando acabe el bucle while .
# Lo que haya dentro de ese else se ejecutará una vez
# acabe la ejecución del while . Lo podrás usar para cuando pierdas.

# SOLUCIÓN:


random_number = random.randint(1, 5)

vidas = 2

while vidas > 0:
    random_choice = random.randint(1, 5)
    if random_choice == random_number:
        break
    else:
        vidas -= 1

if vidas > 0:
    print("You win")
else:
    print("You lose")
