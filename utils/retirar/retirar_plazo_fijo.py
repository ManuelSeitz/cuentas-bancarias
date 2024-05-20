"""Módulo para retirar plazo fijo"""

from typing import List
from clases.plazo_fijo import PlazoFijo
from utils.buscar_cuenta_por_dni import buscar_cuenta_por_dni
from constantes.listas import PLAZOS_FIJOS


def retirar_plazo_fijo() -> None:
    """Retira una cantidad determinada de dinero a una cuenta"""
    print("RETIRAR PLAZO FIJO")

    cuenta = buscar_cuenta_por_dni()

    if cuenta is None:
        print("La cuenta no fue encontrada")
        input("Presiona Enter para continuar")
        return

    # Lista con los plazos fijos de la cuenta
    plazos_fijos_cuenta: List[PlazoFijo] = []

    for plazo_fijo in PLAZOS_FIJOS:
        # Si el plazo fijo pertenece al titular se agrega a la lista
        if plazo_fijo.titular.dni == cuenta.titular.dni:
            plazos_fijos_cuenta.append(plazo_fijo)

    for i, plazo_fijo in enumerate(plazos_fijos_cuenta):
        print(
            f"Plazo fijo {i} - Fecha de vencimiento {plazo_fijo.fecha_vencimiento.date()}"
        )

    while True:
        try:
            indice_plazo_fijo_seleccionado = int(
                input("Seleccione el plazo fijo a operar: ")
            )
            if (
                indice_plazo_fijo_seleccionado < 0
                or indice_plazo_fijo_seleccionado >= len(plazos_fijos_cuenta)
            ):
                raise IndexError

            break
        except ValueError:
            print("Plazo fijo inválido")
        except IndexError:
            print("Plazo fijo fuera de rango")

    while True:
        try:
            cantidad = float(input("Cantidad a retirar: "))
            break
        except ValueError:
            print("Cantidad inválida")

    plazos_fijos_cuenta[indice_plazo_fijo_seleccionado].retirar(cantidad)
    input("Presiona Enter para continuar")
