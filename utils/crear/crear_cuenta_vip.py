"""Módulo para crear una cuenta VIP"""

from clases.cuenta_vip import CuentaVIP
from utils.buscar_cuenta_por_dni import buscar_cuenta_por_dni
from constantes.listas import CUENTAS


def crear_cuenta_vip() -> None:
    """Crea una cuenta VIP"""
    print("CUENTA VIP")

    cuenta = buscar_cuenta_por_dni()

    if cuenta is None:
        print("La cuenta no fue encontrada")
        input("Presiona Enter para continuar")
        return

    while True:
        try:
            saldo_negativo_maximo = float(input("Saldo negativo máximo: "))
            break
        except ValueError:
            print("Saldo inválido")

    cuenta_vip = CuentaVIP(cuenta.titular, saldo_negativo_maximo)

    # Remover la cuenta antigua
    CUENTAS.remove(cuenta)
    # Reemplazarla por cuenta_vip
    CUENTAS.append(cuenta_vip)
    print("Cuenta VIP creada con éxito")
    input("Presiona Enter para continuar")
