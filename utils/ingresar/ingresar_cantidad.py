"""Módulo para ingresar cantidad"""

from utils.buscar_cuenta_por_dni import buscar_cuenta_por_dni


def ingresar_cantidad() -> None:
    """Ingresa una cantidad determinada de dinero a una cuenta"""
    print("INGRESAR CANTIDAD")

    cuenta = buscar_cuenta_por_dni()

    if cuenta is None:
        print("La cuenta no fue encontrada")
        input("Presiona Enter para continuar")
        return

    while True:
        try:
            cantidad = float(input("Cantidad a ingresar: "))
            break
        except ValueError:
            print("Cantidad inválida")

    cuenta.ingresar(cantidad)
    input("Presiona Enter para continuar")
