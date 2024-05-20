"""Módulo para crear cuenta joven"""

from clases.cuenta_joven import CuentaJoven
from utils.buscar_cuenta_por_dni import buscar_cuenta_por_dni
from constantes.listas import CUENTAS


def crear_cuenta_joven() -> None:
    """Crea una cuenta joven"""
    print("CUENTA JOVEN")

    cuenta = buscar_cuenta_por_dni()

    if cuenta is None:
        print("La cuenta no fue encontrada")
        input("Presiona Enter para continuar")
        return

    while True:
        try:
            bonificacion = int(input("Bonificación de la cuenta: "))

            if bonificacion < 0:
                raise ValueError

            break
        except ValueError:
            print("Bonificacion inválida")

    cuenta_joven = CuentaJoven(cuenta.titular, bonificacion)

    if not cuenta_joven.es_titular_valido():
        print("No es titular válido, no puede crear la cuenta")
        input("Presiona Enter para continuar")
        return

    # Remover la cuenta antigua
    CUENTAS.remove(cuenta)
    # Reemplazarla por cuenta_joven
    CUENTAS.append(cuenta_joven)
    print("Cuenta joven creada con éxito")
    input("Presiona Enter para continuar")
