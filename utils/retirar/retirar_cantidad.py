"""Módulo para retirar cantidad"""

from utils.buscar_cuenta_por_dni import buscar_cuenta_por_dni


def retirar_cantidad() -> None:
    """Retira una cantidad determinada de dinero a una cuenta"""
    print("RETIRAR CANTIDAD")

    cuenta = buscar_cuenta_por_dni()

    if cuenta is None:
        print("La cuenta no fue encontrada")
        input("Presiona Enter para continuar")
        return

    while True:
        try:
            cantidad = float(input("Cantidad a retirar: "))
            break
        except ValueError:
            print("Cantidad inválida")

    cuenta.retirar(cantidad)
    input("Presiona Enter para continuar")
