

##### Ejercicio 1.
# Escribe una función que convierta números del 1 al 7 en nombres de los dias de la semana.
# La función constará de un único argumento numérico y una salida de tipo string

def num_dia_semana(numero):
    """Recibe un número y lo convierte al día de la semana correspondiente.

    Params:
        - numero: int
    Return:
        - dia_semana: str
    """

    # Evaluamos si el argumento es realmente numérico
    if not isinstance(numero, int):
        return print("Error. El argumento de la función debe ser un número entero.")
    # Evaluamos también si el número está en el rango (1,8)
    if numero not in range(1,8):
        return print("Error, debes introducir un número entre el 1 y el 7 (inclusive)")

    # Creamos un diccionario con los días de la semana
    dias_semana = {
        1: 'Lunes',
        2: 'Martes',
        3: 'Miércoles',
        4: 'Jueves',
        5: 'Viernes',
        6: 'Sábado',
        7: 'Domingo'}

    # Devolvemos el valor del número introducido, que actúa como clave
    return dias_semana[numero]


##### Ejercicio 2.
# En el ejercicio 8 de bucles, creábamos una pirámide invertida,
# cuyo número de pisos venía determinado por un input del usuario.
# Crea una función que replique el comportamiento de la pirámide,
# y utiliza un único parámetro de entrada de la función para determinar
# el número de filas de la pirámide, es decir, elimina la sentencia input.

# No entiendo lo que hay que hacer

##### Ejercicio 3.
# Escribe una función que compare dos números. La función tiene dos argumentos
# y hay tres salidas posibles: que sean iguales, que el primero sea mayor que el segundo,
# o que el segundo sea mayor que el primero.

def compara_nums(num1, num2):
    """Recibe dos números y realiza una
    comparación entre ellos.

    Params:
        - num1: int, float
        - num2: int, float
    Return:
        - resultado: str, resultado de la comparación
    """
    if num1 > num2:
        return f"El número {num1} es el mayor."
    elif num2 > num1:
        return f"El número {num2} es el mayor."
    else:
        return "Ambos números son iguales."

##### Ejercicio 4.
# Escribe una función que sea un contador de letras. En el primer argumento tienes
# que introducir un texto, y el segundo que sea la letra a contar.
# La función devuelve un entero con el número de veces que aparece esa letra, tanto
# mayúscula como minúscula.

# Definimos la función:
def contador_letras(texto, letra):
    """Recibe un texto y una letra, y devuelve las
    veces que se repite la letra en el texto.

    Params:
        - texto: str, texto a evaluar
        - letra: str, letra a evaluar
    Return:
        - num_veces: int, número de veces que se repite letra en texto
    """
    # Estandarizamos el texto
    texto = texto.lower()

    num_veces = 0

    for caracter in texto:
        if caracter == letra:
            num_veces += 1

    return num_veces


##### Ejercicio 5.
# Escribe una función que tenga un único argumento, un string. La salida de la función
# tiene que ser un diccionario con el conteo de todas las letras de ese string.

def cuenta_letras(string):
    """Recibe un string, y construye un diccionario
    cuyas claves son las letras únicas de ese string,
    y los valores el número de veces que se repite
    cada letra.

    Params:
        - string: str, texto a evaluar
    Return:
        - dicc_letras: dict, diccionario con el conteo de letras
    """

    dicc_letras = {}

    for caracter in string:
        if caracter not in dicc_letras:
            dicc_letras[caracter] = 1
        else:
            dicc_letras[caracter] += 1

    return dicc_letras


##### Ejercicio 6.
# Escribir una función que añada o elimine elementos de una lista. La función necesita
# los siguientes argumentos:
# - lista: la lista donde se añadirán o eliminarán los elementos
# - comando: "add" o "remove"
# - elemento: Por defecto es None.

def agrega_o_elimina(lista, comando, elemento=None):
    """Añade o elimina elementos de una lista.
     La lista, la acción y el elemento los proporciona
     el usuario mediante parámetro.

     Params:
        - lista: list, lista a modificar
        - comando: str, acción a realizar
        - elemento: any, elemento que interactúa con la lista
    Return:
        - lista: list, lista modificada
    """

    # Evaluamos si existe lista y comando
    if not lista or not comando or not elemento:
        return "No se puede realizar la acción"
    # Evaluamos si es válida la acción:
    if comando not in ['add', 'remove']:
        return "Error. Comando no válido"
    # Evaluamos el tipo de comando
    if comando == 'add':
        lista.append(elemento)
    else:
        lista.remove(elemento)

    return lista


##### Ejercicio 7.
# Crea una función que reciba un número arbitrario de palabras, y devuelva la frase
# completa, separando las palabras con espacios.

def crea_frase(*args):
    """Recibe un número indeterminado de palabras,
    y devuelve la frase completa separada por espacios.

    Params:
        - *args: str expected
    Return:
        - frase: str, palabras separadas por espacios
    """

    return " ".join(args)


##### Ejercicio 8.
# Escribe un programa que obtenga el enésimo número de la serie de Fibonacci.
# Hay que crear una función recursiva con un único argumento

# No he sido capaz

##### Ejercicio 9.
# Define en una única celda las siguientes funciones:
# - Función que calcule el área de un cuadrado
# - Función que calcule el area de un triángulo
# - Función que calcule el área de un círculo


# Área de un cuadrado: lado al cuadrado
def area_cuadrado(lado):
    """Calcula el área de un cuadrado a partir de uno de los lados

    Params:
        - lado: int
    Return:
        - area: int
    """
    area = lado ** 2
    return area

# Área de un triángulo: base * altura
def area_triangulo(base, altura):
    """Calcula el área de un triángulo a partir de
    la base y la altura.

    Params:
        - base: int
        - altura: int
    Return:
        - area: int
    """
    area = base * altura / 2
    return area

# Área del círculo: Pi por radio al cuadrado
def area_circulo(radio):
    """Calcula el área de un círculo a partir del radio.

    Params:
        - radio: int
    Return:
        - area: int
    """
    import math

    pi = math.pi
    area = pi * (radio ** 2)

    return area

# En otra celda, calcular el area de:
# - Dos círculos de radio 10 + un triángulo de base 3 y altura 7
# - Un cuadrado de lado = 10 + 3 círculos (uno de radio = 4 y los otros dos de radio = 6) +
# 5 triángulos de base = 2 + altura = 4

a = 2 * area_circulo(radio=10) + area_triangulo(base=3, altura=7)
b = area_cuadrado(lado=10) + area_circulo(radio=4) + 2 * area_circulo(radio=6) \
    + 5 * area_triangulo(base=2, altura=4)