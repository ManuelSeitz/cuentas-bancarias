"""Módulo para crear un plazo fijo"""

from datetime import datetime
from clases.plazo_fijo import PlazoFijo
from utils.buscar_cuenta_por_dni import buscar_cuenta_por_dni
from constantes.listas import PLAZOS_FIJOS


def crear_plazo_fijo() -> None:
    """Crea un plazo fijo"""
    print("PLAZO FIJO")

    cuenta = buscar_cuenta_por_dni()

    if cuenta is None:
        print("La cuenta no fue encontrada")
        input("Presiona Enter para continuar")
        return

    while True:
        try:
            cantidad = float(input("Cantidad dinero plazo fijo: "))
            break
        except ValueError:
            print("Cantidad inválida")

    while True:
        try:
            fecha_vencimiento_str = input(
                "Ingrese la fecha de vencimiento en formato dd/mm/aaaa: "
            )
            fecha_vencimiento = datetime.strptime(fecha_vencimiento_str, "%d/%m/%Y")
            break
        except ValueError:
            print("Fecha inválida")

    plazo_fijo = PlazoFijo(cuenta.titular, cantidad, fecha_vencimiento)

    PLAZOS_FIJOS.append(plazo_fijo)
    print("Plazo fijo creado con éxito")
    input("Presiona Enter para continuar")
