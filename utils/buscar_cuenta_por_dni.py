"""Módulo para buscar cuentas por DNI"""

from clases.cuenta import Cuenta
from clases.cuenta_joven import CuentaJoven
from clases.cuenta_vip import CuentaVIP

from constantes.listas import CUENTAS
from constantes.dni import VALOR_MINIMO_DNI, VALOR_MAXIMO_DNI


def buscar_cuenta_por_dni() -> Cuenta | CuentaJoven | CuentaVIP | None:
    """Itera sobre una cuentas y retorna un diccionario indicando si fue encontrada y su
    titular correspondiente"""

    while True:
        try:
            dni_a_buscar = int(input("DNI a buscar: "))

            if dni_a_buscar < VALOR_MINIMO_DNI or dni_a_buscar > VALOR_MAXIMO_DNI:
                raise ValueError("DNI fuera de rango")

            break
        except ValueError:
            print("DNI inválido")

    for cuenta in CUENTAS:
        if cuenta.titular.dni == dni_a_buscar:
            return cuenta
    return None
