"""Módulo de la clase CuentaVIP"""

from clases.cuenta import Cuenta
from clases.persona import Persona


class CuentaVIP(Cuenta):
    """Definición de la clase CuentaVIP heredada de Cuenta"""

    def __init__(
        self, titular: Persona, saldo_negativo_maximo: float, cantidad: float = None
    ) -> None:
        super().__init__(titular, cantidad)
        # Se asume que el saldo negativo se valida antes de instanciar la clase
        self.saldo_negativo_maximo = saldo_negativo_maximo

    def retirar(self, cantidad_a_retirar: float) -> None:
        if cantidad_a_retirar < 0:
            print("Ingrese un valor positivo")
            return

        cantidad_actual = self.get_cantidad()
        nueva_cantidad = cantidad_actual - cantidad_a_retirar

        if nueva_cantidad < self.saldo_negativo_maximo:
            print("Se excedió el saldo negativo máximo, no puede retirar dinero.")
            return

        if self.set_cantidad(nueva_cantidad):
            print("Cantidad retirada con éxito")
        else:
            print("Fallo en la transacción")
