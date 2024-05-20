"""Módulo para buscar cuentas por DNI"""

from clases.cuenta import Cuenta
from clases.cuenta_joven import CuentaJoven
from clases.cuenta_vip import CuentaVIP
from constantes.listas import CUENTAS


def buscar_cuenta_por_dni() -> Cuenta | CuentaJoven | CuentaVIP | None:
    """Itera sobre una cuentas y retorna un diccionario indicando si fue encontrada y su
    titular correspondiente"""

    while True:
        try:
            dni_a_buscar = int(input("DNI a buscar: "))
            # Establecer valor mínimo y máximo para el DNI
            # En este caso es especifico para Argentina
            valor_minimo_dni = 10000000
            valor_maximo_dni = 99999999

            if dni_a_buscar < valor_minimo_dni or dni_a_buscar > valor_maximo_dni:
                raise ValueError("DNI fuera de rango")

            break
        except ValueError:
            print("DNI inválido")

    for cuenta in CUENTAS:
        if cuenta.titular.dni == dni_a_buscar:
            return cuenta
    return None
