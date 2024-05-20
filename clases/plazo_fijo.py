"""Módulo de la clase PlazoFijo"""

from datetime import datetime
from clases.cuenta import Cuenta
from clases.persona import Persona


class PlazoFijo(Cuenta):
    """Definición de la clase CuentaJoven heredada de Cuenta"""

    def __init__(
        self, titular: Persona, cantidad: float, fecha_vencimiento: datetime
    ) -> None:
        super().__init__(titular, cantidad)
        # Se da por hecho que la validación de la fecha de vencimiento se hace
        # antes de crear la instancia
        self.fecha_vencimiento = fecha_vencimiento

    def retirar(self, cantidad_a_retirar: float) -> None:
        dia_actual: datetime = datetime.today()

        # Si aún no llega la fecha de vencimiento, se hace el procedimiento normalmente
        if dia_actual < self.fecha_vencimiento:
            super().retirar(cantidad_a_retirar)
            return

        # Penalización del 5%
        penalizacion = 5
        decimal_penalizacion = penalizacion / 100
        monto_penalizacion_calculado = cantidad_a_retirar * decimal_penalizacion

        # Se le suma el monto de penalización a la cantidad a retirar original
        cantidad_a_retirar += monto_penalizacion_calculado

        cantidad_actual = self.cantidad
        nueva_cantidad = cantidad_actual - cantidad_a_retirar

        if self.set_cantidad(nueva_cantidad):
            print(
                f"Cantidad retirada con éxito, se aplicó una penalización del {penalizacion}%"
            )
        else:
            print("Fallo en la transacción")
