"""Módulo de la clase CuentaJoven"""

from clases.cuenta import Cuenta
from clases.persona import Persona


class CuentaJoven(Cuenta):
    """Definición de la clase CuentaJoven heredada de Cuenta"""

    def __init__(
        self,
        titular: Persona,
        bonificacion: int,
        cantidad: float = 0,
    ) -> None:
        """
        ARGS:
        bonificacion (int): Representa un numero entero indicando el porcentaje
        de la bonificación (ejemplo: 10 -> 10%)
        """
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def get_bonificacion(self) -> int:
        """Devuelve el valor del atributo bonificacion"""
        return self.bonificacion

    def set_bonificacion(self, bonificacion: int) -> None:
        """Modifica el valor del atributo titular"""
        try:
            if bonificacion < 0:
                raise ValueError
            self.bonificacion = int(bonificacion)
        except ValueError:
            print("Bonificación inválida")

    def es_titular_valido(self) -> bool:
        """Devuelve True si el titular es mayor de edad y menor de 25 años
        False en caso contrario"""
        return self.titular.edad >= 18 and self.titular.edad < 25

    # Sobrescribir método ingresar para aplicar la bonificación
    def ingresar(self, cantidad_a_ingresar: float) -> None:
        if cantidad_a_ingresar < 0:
            print("Ingrese un valor positivo")
            return

        cantidad_actual = self.get_cantidad()
        # Se le suma a la cantidad actual la cantidad a ingresar + un extra
        # respecto a la cantidad que se ingresó
        nueva_cantidad = (
            cantidad_actual
            + cantidad_a_ingresar
            + (cantidad_a_ingresar * (self.get_bonificacion() / 100))
        )

        if self.set_cantidad(nueva_cantidad):
            print("Cantidad ingresada con éxito")
            print(f"Aplicada la bonificación del {self.get_bonificacion()}%")
            print(f"Cantidad actual: {self.cantidad}")
        else:
            print("Fallo en la transacción")

    def retirar(self, cantidad_a_retirar: float) -> None:
        if not self.es_titular_valido():
            print("El titular no es válido para retirar dinero")
            return
        super().retirar(cantidad_a_retirar)

    def mostrar_datos(self) -> None:
        # En el ejercicio dice que sólo debe mostrar "Cuenta joven" y la bonificación
        # Si se debe mostrar el resto de datos entonces descomenten el método
        print("Cuenta joven")
        print(f"Bonificación: {self.get_bonificacion()}%")

        # super().mostrar_datos()
