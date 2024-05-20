"""Módulo de la clase Cuenta"""

from clases.persona import Persona


class Cuenta:
    """Definición de la clase Cuenta"""

    def __init__(self, titular: Persona, cantidad: float = 0) -> None:
        # Se asume que el titular se valida antes de instanciar la clase
        self.titular = titular
        self.cantidad = cantidad

    def get_titular(self) -> Persona:
        """Devuelve el valor del atributo titular"""
        return self.titular

    def set_titular(self, titular: Persona) -> None:
        """Modifica el valor del atributo titular"""
        # Validar que titular sea instancia de persona
        if not isinstance(titular, Persona):
            print("Ingrese un titular válido")
            return
        self.titular = titular

    def get_cantidad(self) -> float:
        """Devuelve el valor del atributo cantidad"""
        return self.cantidad

    def set_cantidad(self, cantidad: float) -> bool:
        """
        Modifica el valor del atributo cantidad, retorna un valor lógico:
        True: Transacción realizada con éxito.
        False: Transacción fallida.
        """
        try:
            # Tira un error si la conversión falla
            cantidad = float(cantidad)

            self.cantidad = cantidad
            return True
        except ValueError:
            print("Cantidad inválida")
            return False

    def mostrar_datos(self) -> None:
        """Muestra los datos de la cuenta"""
        print("Datos de la cuenta".center(120))
        print(f"DNI del titular: {self.titular.dni}")
        print(f"Nombre del titular: {self.titular.nombre}")
        print(f"Cantidad: {self.cantidad}")

    def ingresar(self, cantidad_a_ingresar: float) -> None:
        """Método público por el cual se ingresa dinero a la cuenta"""
        if cantidad_a_ingresar < 0:
            print("Ingrese un valor positivo")
            return

        cantidad_actual = self.get_cantidad()
        nueva_cantidad = cantidad_actual + cantidad_a_ingresar

        if self.set_cantidad(nueva_cantidad):
            print("Cantidad ingresada con éxito")
        else:
            print("Fallo en la transacción")
            raise ValueError

    def retirar(self, cantidad_a_retirar: float) -> None:
        """Método público por el cual se retira dinero de la cuenta"""
        if cantidad_a_retirar < 0:
            print("Ingrese un valor positivo")
            return

        cantidad_actual = self.get_cantidad()
        nueva_cantidad = cantidad_actual - cantidad_a_retirar

        # Para que la cuenta VIP tenga sentido agregué esto
        # Las cuentas que no sean VIP pueden tener un corto margen negativo
        margen_cantidad_negativa = -20000
        if nueva_cantidad < margen_cantidad_negativa:
            print("No es posible retirar el dinero, margen negativo excedido")
            raise ValueError

        if self.set_cantidad(nueva_cantidad):
            print("Cantidad retirada con éxito")
        else:
            print("Fallo en la transacción")
            raise ValueError
