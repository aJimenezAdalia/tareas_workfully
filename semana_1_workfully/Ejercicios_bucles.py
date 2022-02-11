


##### Ejercicio 1
# 1. Elimina todos los VW de la siguiente lista. Crea una lista nueva para ello.
# 2. Hazlo de otra manera. Crea una lista nueva vacía, y ve añadiendo todos los que
# no sean VW
# 3. En vez de for , usa un bucle while

# 1.
ejer_1 = ["VW", "Audi", "Renault", "VW", "BMW"]
lista_ejer_1_1 = [elem for elem in ejer_1 if elem != "VW"]

# 2.
lista_ejer_1_2 = []
for elem in ejer_1:
    if elem != "VW":
        lista_ejer_1_2.append(elem)

# 3.
lista_ejer_1_3 = []
contador = 0

while contador < len(ejer_1):
    if ejer_1[contador] != "VW":
        lista_ejer_1_3.append(ejer_1[contador])
    contador += 1

print(lista_ejer_1_3)


##### Ejercicio 2.
# Imprime por pantalla la siguiente secuencia: 10,9,8 ... -8,-9,-10
lista_ejer_2 = list(range(-10,11))
lista_ejer_2.reverse()
for i in lista_ejer_2:
    print(i)

##### Ejercicio 3.
# 1. Escribe un programa que vaya pidiendo numeros al usuario.
# Cuando el usuario introduzca el 0, el programa tiene que imprimir por
# pantalla el sumatorio de todos los numeros positivos introducidos

contador_ejercicio_3 = 0

while True:
    entrada_usuario = int(input("Introduce un número: "))
    if entrada_usuario != 0:
        if entrada_usuario > 0:
            contador_ejercicio_3 += entrada_usuario
    else:
        break

print(f"La suma total es: {contador_ejercicio_3}")

# 2. Además de la suma, queremos que imprima también una lista con todos los números.

contador_ejercicio_3 = 0
lista_todos_numeros = []

while True:
    entrada_usuario = int(input("Introduce un número: "))
    # Sea cual sea la entrada, la agregamos a la lista
    lista_todos_numeros.append((entrada_usuario))

    if entrada_usuario != 0:
        if entrada_usuario > 0:
            contador_ejercicio_3 += entrada_usuario
    else:
        break

print(f"La suma total es: {contador_ejercicio_3}")
print(f"Los números introducidos fueron {lista_todos_numeros}")


##### Ejercicio 4.
# Escribir un programa que vaya pidiendo la cantidad de compras que hace un cliente
# en una página web. El programa tiene que pedir cantidades hasta que se ingresa un 0.
# Igualmente cuando una de las cantiaddes introducida es negativa, hay que imprimir por
# pantalla un mensaje:
# "Numero negativo, por favor, introduzca un numero positivo"

cantidad_total = 0

while True:
    cantidad = input("Ingrese una cantidad: ")
    try:
        cantidad = int(cantidad)
    except ValueError:
        print("Error. Introduzca un número, por favor")
        continue

    if cantidad < 0:
        print("Número negativo, por favor, introduzca un número positivo.")
    elif cantidad == 0:
        print(f"Bucle finalizado. Cantidad total: {cantidad_total}")
        break
    else:
        cantidad_total += cantidad

##### Ejercicio 5
# Imprime por pantalla la palabra "Python" pero empezando por la última letra
palabra = "Python"
print(palabra[::-1])

##### Ejercicio 6.
# Escribe un programa que calcule la cantidad de veces que está la letra
# "m" o "M" en la frase:
frase = "En un lugar de La Mancha, de cuyo nombre no quiero acordarme"

cantidad_veces = 0

for letra in frase:
    if letra == "m" or letra == "M":
        cantidad_veces += 1

print(f"En la frase se repite la m o la M {cantidad_veces} veces")

###### Ejercicio 7.
# Crea un programa que simule la siguiente pirámide. Para ello,
# el programa tiene que pedirle al usuario un caracter cualquiera.
# El número de filas fijo es 5

def piramide(caracter):
    """Recibe un caracter, y muestra por pantalla
    una pirámide con el caracter recibido.

    Params:
        - caracter: str
    """
    caracter += " "

    for i in range(-5, 0):
        print(caracter * -i)

# Comprobación:
piramide("W")


##### Ejercicio 8.
# Crea un programa que en función de un input numérico que inserte el usario,
# imprima por pantalla la pirámide de ejemplo. Si el input es 6, tendrá seis
# pisos, pero si introduce 10, la pirámide tendrá 10 pisos.

'''
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3 
1 2 
1
'''

def piramide_pisos(num_pisos):
    """Imprime por pantalla una pirámide, cuyo número
    de pisos viene indicado por el parámetro recibido.

    Params:
        - num_pisos: int
    """

    while num_pisos >= 1:
        lista_strings = [str(-i) for i in range(-num_pisos, 0)]
        lista_strings.reverse()
        print(" ".join(lista_strings))
        num_pisos -= 1


##### Ejercicio 10.
# Imprime toda la secuencia de números del 1 al 10, excepto el 3,4 y 9.
# Impleméntalo de dos maneras diferentes

# 1. Con un bucle for
lista_nums = [i for i in range(1, 11) if i not in [3, 4, 9]]
for i in lista_nums:
    print(i)

# 2. Con un bucle while
numero = 1

while numero < 11:
    if numero not in [3, 4, 9]:
        print(numero)
        numero += 1
    else:
        numero += 1


##### Ejercicio 11.
# Suponiendo que siempre se cumple que las dos listas del ejercicio
# son iguales de tamaño, implementa un programa que calcule el ratio
# ingreso/gasto de cada elemento, y lo guarde en una nueva lista.
# Si hubiese algún problema con los datos, hay que almacenar un mensaje
# de error en la lista del resultado. Usa try/except

ingresos = [100, 200, 500, 100, 600]
gastos = [50, 20, 70, 0, 25]

# Creamos una lista vacía para almacenar los resultados
resultados = []

# Iteramos sobre ambas listas y vamos calculando los ratios

for ingreso, gasto in zip(ingresos, gastos):
    # El único problema que podemos tener es una división por cero, entonces:
    try:
        ratio = ingreso/gasto
        resultados.append(ratio)
    except ZeroDivisionError:
        resultados.append("Error en el cálculo")


##### Ejercicio 12.
# Muy parecido al anterior, aunque ahora tendremos que excepcionar más tipos
# de errores con estos nuevos datos. En este caso, almacena un mensaje diferente
# en la lista resultado, para cada error.

ingresos = [100, "HHH", 500, 100, 600, 900, 150]
gastos = [50, 20, 70, 0, 25]

ratios = []

# Hacemos lo mismo que antes pero utilizamos "exception as e"
for ingreso, gasto in zip(ingresos, gastos):
    try:
        ratio = ingreso/gasto
        ratios.append(ratio)
    except Exception as e:
        ratios.append(e)




