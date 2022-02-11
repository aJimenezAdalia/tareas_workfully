


# 1. Implementar la clase "Tienda"

print('1. Creando clase Tienda...')

class Tienda:
    tipo = 'electrodomésticos'
    abierta = True

    def __init__(self, nombre, direccion, num_empleados, ventas_ult_3_meses):
        """Constructor de la clase Tienda.

        Params:
            - nombre: str, nombre de la tienda
            - direccion: str, dirección de la tienda
            - num_empleados: int, nº de empleados de la tienda
            - ventas_ult_3_meses: list, ventas de los últimos 3 meses
        """
        self.nombre = nombre
        self.direccion = direccion
        self.num_empleados = num_empleados
        self.ventas_ult_3_meses = ventas_ult_3_meses

    def ventas_totales(self):
        """Devuelve la suma de las ventas de los últimos tres meses
        """
        return sum(self.ventas_ult_3_meses)

    def media_ventas_empleado(self):
        """Devuelve la media de ventas de los últimos meses por empleado
        """
        return self.ventas_totales() / self.num_empleados

    def datos_tienda(self):
        """Devuelve el nombre de la tienda y su dirección
        """
        return f'- Nombre de la tienda: {self.nombre}\n- Dirección: {self.direccion}'

    def ventas_ultimo_mes(self):
        """Devuelve las ventas totales del último mes
        """
        return self.ventas_ult_3_meses[-1]

    def proyeccion_ventas(self, inversion_marketing):
        """Devuelve las ventas esperadas en caso de invertir una cantidad
        (recibida por parámetro) en márketing.

        Params:
            - inversion_marketing: int expected, inversión en márketing
        """
        if inversion_marketing < 1000:
            return 1.2 * self.ventas_totales()
        else:
            return 1.5 * self.ventas_totales()

print('Clase creada con éxito.')


# 2. Crear tres tiendas con datos inventados

print('\n2. Creando tres tiendas...')

# Tienda 1:
tienda_1 = Tienda(
    nombre='tienda_1',
    direccion='Calle Mayor, 4',
    num_empleados=25,
    ventas_ult_3_meses=[15000, 17000, 9000])

# Tienda 2:
tienda_2 = Tienda(
    nombre='tienda_2',
    direccion='Avenida Real, 10',
    num_empleados=20,
    ventas_ult_3_meses=[10000, 11000, 7000])

# Tienda 3:
tienda_3 = Tienda(
    nombre='tienda_3',
    direccion='Paseo Recoletos, 15',
    num_empleados=30,
    ventas_ult_3_meses=[21000, 18000, 11000])

print('Tiendas creadas con éxito.\n')

# 3 Comprobar en una de ellas lo implementado:

print(f'- 3.1. Comprobando atributos de "tienda_1":')
print(f'- Tipo:', tienda_1.tipo)
print(f'- Abierta:', tienda_1.abierta)
print(f'- Nombre:', tienda_1.nombre)
print(f'- Dirección:', tienda_1.direccion)
print(f'- Nº Empleados:', tienda_1.num_empleados)
print(f'- Ventas últimos 3 meses:', tienda_1.ventas_ult_3_meses)

print(f'\n- 3.2. Comprobando métodos de "tienda_1":')
print(f'- Ventas totales:', tienda_1.ventas_totales())
print(f'- Media de ventas por empleado:', tienda_1.media_ventas_empleado())
print(f'- Datos de la tienda:', tienda_1.datos_tienda())
print(f'- Ventas último mes:', tienda_1.ventas_ultimo_mes())
print(f'- Proyección ventas (inversión de 1000€):', tienda_1.proyeccion_ventas(1000))

print('Comprobaciones completadas con éxito.')

# 4. Calcular las ventas del último mes de todas las tiendas. Usar un for

tiendas = [tienda_1, tienda_2, tienda_3]
ventas_ult_mes_todas_tiendas = 0

print('\n- 4. Calculando ventas del último mes (todas las tiendas)...')

for tienda in tiendas:
    ventas_ult_mes_todas_tiendas += tienda.ventas_ultimo_mes()

print(f'- Ventas totales último mes:', ventas_ult_mes_todas_tiendas)

# 5. Imprimir las tiendas cuya dirección contenga "Avenida"

print('\n5. Tiendas donde "Avenida" aparezca en su dirección:')

for tienda in tiendas:
    if 'Avenida' in tienda.direccion:
        print(f'- La tienda {tienda.nombre} contiene la palabra "Avenida".')

# 6. Documentación

# Hecho



