"""Módulo de la clase Persona"""

from re import fullmatch
from constantes.dni import VALOR_MINIMO_DNI, VALOR_MAXIMO_DNI


class Persona:
    """Definición de la clase Persona"""

    def __init__(self, nombre: str = "", edad: int = None, dni: int = None) -> None:
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def get_nombre(self) -> str:
        """Devuelve el valor del atributo nombre"""
        return self.nombre

    def set_nombre(self, nombre: str) -> None:
        """Modifica el valor del atributo nombre"""
        # Validado con expresión regular
        # De esta forma un nombre no puede contener números ni caracteres especiales
        if not fullmatch(r"^[a-zA-Zá-úÁ-Ú\s']+$", nombre):
            print("El nombre no es válido")
            return
        self.nombre = nombre

    def get_edad(self) -> int:
        """Devuelve el valor del atributo edad"""
        return self.edad

    def set_edad(self, edad: int) -> None:
        """Modifica el valor del atributo edad"""
        try:
            # Tira un error si la conversión falla
            self.edad = int(edad)

            # Tira un error si se cumple la condición
            if edad < 0 or edad > 120:
                raise ValueError

        # Manejar el error
        except ValueError:
            print("La edad no es válida")

    def get_dni(self) -> int:
        """Devuelve el valor del atributo dni"""
        return self.dni

    def set_dni(self, dni: int) -> None:
        """Modifica el valor del atributo dni"""

        try:
            # Tira un error si la conversión falla
            self.dni = int(dni)

            # Tira un error si se cumple la condición
            if dni < VALOR_MINIMO_DNI or dni > VALOR_MAXIMO_DNI:
                raise ValueError("DNI fuera de rango")

        # Manejar el error
        except ValueError:
            print("El DNI no es válido")

    def mostrar_datos(self) -> None:
        """Muestra los datos de la persona"""
        print("Datos personales".center(120))
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")

    def es_mayor_edad(self) -> bool:
        """Retorna un valor lógico dependiendo si es mayor de edad o no"""
        return self.edad >= 18
