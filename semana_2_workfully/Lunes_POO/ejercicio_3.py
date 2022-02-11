

# Ejercicio 3. Adaptación de la clase Tienda para tiendas Decathlon

class TiendaDecathlon:
    tipo = 'Deportes'
    abierta = True

    def __init__(self, tipo, nombre, direccion, num_empleados, ventas_ult_ano, gastos_ultimo_ano):
        """Constructor de la clase TiendaDecathlon.

        Params:
            - tipo: str,
            - nombre: str, nombre de la tienda
            - direccion: str, dirección de la tienda
            - num_empleados: int, nº de empleados de la tienda
            - ventas_ult_ano: list, ventas de los últimos 12 meses
            - gastos_ult_ano: list, gastos de los últimos 12 meses
        """
        self.tipo = tipo
        self.nombre = nombre
        self.direccion = direccion
        self.num_empleados = num_empleados
        self.ventas_ult_ano = ventas_ult_ano
        self.gastos_ultimo_ano = gastos_ultimo_ano

    def ventas_totales(self):
        """Devuelve la suma de las ventas de los últimos doce meses
        """
        return sum(self.ventas_ult_ano)

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
        return self.ventas_ult_ano[-1]

    def proyeccion_ventas(self, inversion_marketing=None):
        """Devuelve las ventas esperadas en caso de invertir una cantidad
        (recibida por parámetro) en márketing.

        Params:
            - inversion_marketing: int expected, default=None, inversión en márketing
        """
        if self.tipo.lower() == 'decathlon city':
            return 'Las tiendas City no trabajan con márketing.'
        if inversion_marketing < 1000:
            return 1.2 * self.ventas_totales()
        else:
            return 1.5 * self.ventas_totales()

    def gastos_ult_ano(self):
        """Devuelve el total de gastos del último año. Si la tienda es Decathlon
        City, se le suma un 10% por sobrecoste de logística y transporte.
        """
        if self.tipo.lower() == 'decathlon city':
            return sum(self.gastos_ultimo_ano) + 0.1 * sum(self.gastos_ultimo_ano)
        return sum(self.gastos_ultimo_ano)


# Comprobación de atributos:

print('- Comprobación de atributos:')
print('Creando dos objetos de TiendaDecathlon...')

# Decathlon tipo 'City'
decathlon_city_goya = TiendaDecathlon(
    tipo = 'Decathlon City',
    nombre = 'Decathlon City Goya',
    direccion = 'Calle Goya, 40 Madrid',
    num_empleados = 40,
    ventas_ult_ano = [
        50000, 45000, 61000, 68000, 66000, 81000,
        40000, 31000, 70000, 60000, 100000, 125000],
    gastos_ultimo_ano = [
        40000, 40000, 47000, 45000, 46000, 56000,
        42000, 37000, 40000, 51000, 60000, 60000])

# Decathlon tipo almacén
decathlon_alcorcon = TiendaDecathlon(
    tipo = 'Decathlon',
    nombre = 'Decathlon Alcorcón',
    direccion = 'Parque Oeste, S/N Alcorcón',
    num_empleados = 90,
    ventas_ult_ano = [
        250000, 245000, 361000, 368000, 366000, 481000,
        240000, 181000, 270000, 360000, 400000, 625000],
    gastos_ultimo_ano = [
        140000, 140000, 147000, 145000, 146000, 156000,
        142000, 137000, 240000, 251000, 260000, 360000])

print('- Dos clases creadas; una tipo City y otra tipo almacén.')
print('\n- Comprobando atributos (tipo City):')
print(f'- Tipo:', decathlon_city_goya.tipo)
print(f'- Nombre:', decathlon_city_goya.nombre)
print(f'- Dirección:', decathlon_city_goya.direccion)
print(f'- Nº Empleados:', decathlon_city_goya.num_empleados)
print(f'- Ventas último año:', decathlon_city_goya.ventas_ult_ano)
print(f'- Gastos último año:', decathlon_city_goya.gastos_ultimo_ano)

print('\n- Comprobando métodos (tipo City):')
print(f'- Ventas totales:', decathlon_city_goya.ventas_totales())
print(f'- Media Ventas por Empleado:', decathlon_city_goya.media_ventas_empleado())
print(f'- Datos de la tienda:', decathlon_city_goya.datos_tienda())
print(f'- Ventas último mes:', decathlon_city_goya.ventas_ultimo_mes())
print(f'- Proyección de Ventas:', decathlon_city_goya.proyeccion_ventas())
print(f'- Gastos último año:', decathlon_city_goya.gastos_ult_ano())

print('Comprobación finalizada (tipo City).')

print('\n- Comprobando tipo almacén:')

print('\n- Comprobando atributos (tipo almacén):')
print(f'- Tipo:', decathlon_alcorcon.tipo)
print(f'- Nombre:', decathlon_alcorcon.nombre)
print(f'- Dirección:', decathlon_alcorcon.direccion)
print(f'- Nº Empleados:', decathlon_alcorcon.num_empleados)
print(f'- Ventas último año:', decathlon_alcorcon.ventas_ult_ano)
print(f'- Gastos último año:', decathlon_alcorcon.gastos_ultimo_ano)

print('\n- Comprobando métodos (tipo almacén):')
print(f'- Ventas totales:', decathlon_alcorcon.ventas_totales())
print(f'- Media Ventas por Empleado:', decathlon_alcorcon.media_ventas_empleado())
print(f'- Datos de la tienda:', decathlon_alcorcon.datos_tienda())
print(f'- Ventas último mes:', decathlon_alcorcon.ventas_ultimo_mes())
print(f'- Proyección de Ventas:', decathlon_alcorcon.proyeccion_ventas(15000))
print(f'- Gastos último año:', decathlon_alcorcon.gastos_ult_ano())

