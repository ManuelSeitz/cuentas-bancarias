"""Módulo para realizar transferencia"""

from utils.buscar_cuenta_por_dni import buscar_cuenta_por_dni


def realizar_transferencia() -> None:
    """Realiza transferencia de una cuenta a otra"""
    print("REALIZAR TRANSFERENCIA")

    print("CUENTA ORDENANTE")
    cuenta_ordenante = buscar_cuenta_por_dni()

    if cuenta_ordenante is None:
        print("La cuenta no fue encontrada")
        input("Presiona Enter para continuar")
        return

    print("CUENTA BENEFICIARIA")
    cuenta_beneficiaria = buscar_cuenta_por_dni()

    if cuenta_beneficiaria is None:
        print("La cuenta no fue encontrada")
        input("Presiona Enter para continuar")
        return

    while True:
        try:
            cantidad = float(input("Cantidad a transferir: "))
            break
        except ValueError:
            print("Cantidad inválida")

    try:
        cuenta_ordenante.retirar(cantidad)
    except ValueError:
        print("Fallo en la transacción")
        return

    try:
        cuenta_beneficiaria.ingresar(cantidad)
    except ValueError:
        print("Fallo en la transferencia")
        # Devuelve la cantidad al ordenante
        cuenta_ordenante.ingresar(cantidad)
        input("Presiona Enter para continuar")
        return

    print("Transferencia exitosa")
    input("Presiona Enter para continuar")
