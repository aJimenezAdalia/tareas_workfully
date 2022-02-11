
# EJERCICIO 2
#
# En este ejercicio vamos a implementar una clase Perro en Python.
# La clase tiene las siguientes características:
# - Cosas que sabemos seguro que tiene un perro
#   - Tiene 4 patas
#   - 2 orejas
#   - 2 ojos
#   - Una velocidad de 0. Por defecto, el perro está parado
# - Cuando se inicialice:
#   - El perro será de una determinada raza
#   - Por defecto tendrá pelo "Marrón", a no ser que se diga lo contrario.
#   - Por defecto no tendrá dueño, a no ser que se diga lo contrario.
# - Dispondrá también de un método llamado andar, que tiene un argumento de entrada
# (aumento_velocidad). Este valor se le sumará a la velocidad que ya llevaba el perro.
# - Necesita otro método (parar), donde pondremos la velocidad a 0.
# - Otro método llamado "ladrar", que tendrá un argumento de entrada,
# y la salida será el siguiente string: "GUAU!" + el argumento de entrada.

# Se pide:
# - 1. Implementa la clase Perro
# - 2. Crea un objeto de tipo Perro, sin dueño
# - 3. Comprueba que están bien todos sus atributos
# - 4. Prueba que ande, y comprueba su velocidad
# - 5. Páralo
# - 6. Documenta la clase Perro


# 1. Implementación de la clase perro:

class Perro:
    """Crea un objeto tipo Perro. Por defecto, tiene cuatro variables:
    - patas=4, orejas=2, ojos=2, velocidad=0
    """
    patas = 4
    orejas = 2
    ojos = 2
    velocidad = 0

    def __init__(self, raza, color_pelo = 'marrón', dueno = None):
        """Constructor de la clase Perro.

        Params:
            - raza: str, raza del perro
            - color_pelo: str, default:marrón, color del pelo del perro
            - dueno: str, default:None, indica si el perro tiene dueño
        """
        self.raza = raza
        self.color_pelo = color_pelo
        self.dueno = dueno

    def andar(self, aumento_velocidad):
        """Recibe por parámetro un número que indica el aumento
        de velocidad que tendrá el objeto perro.

        Params:
            - aumento_velocidad: float or int expected
        """
        self.velocidad += aumento_velocidad

    def parar(self):
        """Cambia el valor de la velocidad del perro a cero
        """
        self.velocidad = 0

    def ladrar(self, ladrido):
        """Recibe un string por parámetro que se imprimirá a
        continuación del string 'GUAU!', a modo de ladrido.

        Params:
            - ladrido: str
        """
        return f'GUAU! {ladrido}'

# 2. Crear un objeto de tipo Perro, sin dueño

# Por defecto, un objeto de tipo Perro no tiene dueño:
perro_sin_dueno = Perro(raza='Pastor Alemán')

# 3. Comprobar que están bien todos los atributos

# Creamos un objeto Perro:
mi_beagle = Perro(
    raza='beagle',
    color_pelo='negro y marrón',
    dueno='Antonio')

# Comprobamos los atributos

print('COMPROBANDO ATRIBUTOS:')

print('nº patas:', mi_beagle.patas)
print('nº orejas:', mi_beagle.orejas)
print('nº ojos:', mi_beagle.ojos)
print('velocidad:', mi_beagle.velocidad)
print('raza:', mi_beagle.raza)
print('color del pelo:', mi_beagle.color_pelo)
print('dueño:', mi_beagle.dueno)
print('\n')

# 4. Prueba que ande, comprueba su velocidad
mi_beagle.andar(aumento_velocidad=5)
print('Perro andando; COMPROBANDO VELOCIDAD:')
print(mi_beagle.velocidad)
print('\n')

# 5. Páralo
mi_beagle.parar()
print('Perro parado; COMPROBANDO VELOCIDAD:')
print(mi_beagle.velocidad)

# 6. Documentación

# Hecho


