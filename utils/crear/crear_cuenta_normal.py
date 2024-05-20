"""Módulo para crear una cuenta normal"""

from clases.cuenta import Cuenta
from constantes.listas import CUENTAS
from utils.crear.crear_titular import crear_titular


def crear_cuenta_normal() -> None:
    """Crea una cuenta normal"""
    titular = crear_titular()

    cuenta = Cuenta(titular)
    CUENTAS.append(cuenta)
    print("Cuenta creada con éxito")
    input("Presiona Enter para continuar")
