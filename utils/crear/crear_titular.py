"""Módulo de creación de titular"""

from re import fullmatch
from clases.persona import Persona

from constantes.listas import CUENTAS
from constantes.dni import VALOR_MINIMO_DNI, VALOR_MAXIMO_DNI


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

            if dni < VALOR_MINIMO_DNI or dni > VALOR_MAXIMO_DNI:
                raise ValueError

            if any(cuenta.titular.dni == dni for cuenta in CUENTAS):
                print("Esta cuenta ya existe")
                continue

            break
        except ValueError:
            print("DNI inválido")

    titular = Persona(nombre, edad, dni)
    return titular
