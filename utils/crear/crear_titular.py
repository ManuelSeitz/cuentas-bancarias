"""Módulo de creación de titular"""

from re import fullmatch
from clases.persona import Persona
from constantes.listas import CUENTAS


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
