"""Módulo principal donde se ejecuta el programa"""

from re import fullmatch
from datetime import datetime
from typing import List
from clases.persona import Persona
from clases.cuenta import Cuenta
from clases.cuenta_joven import CuentaJoven
from clases.cuenta_vip import CuentaVIP
from clases.plazo_fijo import PlazoFijo

# Lista donde se almacenan todas las cuentas
CUENTAS: List[Cuenta | CuentaJoven | CuentaVIP] = []

# Lista donde se almacenan los plazos fijos
PLAZOS_FIJOS: List[PlazoFijo] = []


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


def crear_titular() -> Persona:
    """Crea un titular"""
    print("TITULAR")

    while True:
        nombre = input("Nombre: ")
        if not fullmatch(r"^[a-zA-Zá-úÁ-Ú\s']+$", nombre):
            print("El nombre no es válido")
        else:
            break

    while True:
        try:
            edad = int(input("Edad: "))

            if edad < 0 or edad > 120:
                raise ValueError

            break
        except ValueError:
            print("Edad inválida")

    while True:
        try:
            dni = int(input("DNI: "))
            # Establecer valor mínimo y máximo para el DNI
            # En este caso es especifico para Argentina
            valor_minimo_dni = 10000000
            valor_maximo_dni = 99999999

            if dni < valor_minimo_dni or dni > valor_maximo_dni:
                raise ValueError("DNI fuera de rango")

            if any(cuenta.titular.dni == dni for cuenta in CUENTAS):
                print("Esta cuenta ya existe")
                continue

            break
        except ValueError:
            print("DNI inválido")

    titular = Persona(nombre, edad, dni)
    return titular


def crear_cuenta_normal() -> None:
    """Crea una cuenta normal"""
    titular = crear_titular()

    cuenta = Cuenta(titular)
    CUENTAS.append(cuenta)
    print("Cuenta creada con éxito")
    input("Presiona Enter para continuar")


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

    cuenta_ordenante.retirar(cantidad)
    cuenta_beneficiaria.ingresar(cantidad)

    input("Presiona Enter para continuar")


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


while True:
    print("CUENTAS BANCARIAS".center(120))
    print(
        """
    1.Crear cuenta normal
    2.Crear cuenta joven (a partir de cuenta normal)
    3.Crear cuenta vip (a partir de cuenta normal)
    4.Crear plazo fijo
    5.Ingresar cantidad
    6.Retirar cantidad
    7.Realizar transferencia
    8.Retirar plazo fijo
    0.Salir
    """
    )
    OPCION = None
    while True:
        try:
            OPCION = int(input("Seleccione una operación: "))
            break
        except ValueError:
            print("Ingrese un valor válido")
    match (OPCION):
        case 0:
            break
        case 1:
            crear_cuenta_normal()
        case 2:
            crear_cuenta_joven()
        case 3:
            crear_cuenta_vip()
        case 4:
            crear_plazo_fijo()
        case 5:
            ingresar_cantidad()
        case 6:
            retirar_cantidad()
        case 7:
            realizar_transferencia()
        case 8:
            retirar_plazo_fijo()
        case _:
            print("La operación no es válida")
            input("Presiona Enter para continuar")
