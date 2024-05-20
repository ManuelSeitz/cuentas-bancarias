"""Módulo principal donde se ejecuta el programa"""

from constantes.listas import CUENTAS

# Importar funciones de creación
from utils.crear.crear_cuenta_normal import crear_cuenta_normal
from utils.crear.crear_cuenta_joven import crear_cuenta_joven
from utils.crear.crear_cuenta_vip import crear_cuenta_vip
from utils.crear.crear_plazo_fijo import crear_plazo_fijo

# Importar funciones de ingreso
from utils.ingresar.ingresar_cantidad import ingresar_cantidad

# Importar funciones de retiro
from utils.retirar.retirar_cantidad import retirar_cantidad
from utils.retirar.retirar_plazo_fijo import retirar_plazo_fijo

# Importar funciones de transferencia
from utils.transferir.realizar_transferencia import realizar_transferencia

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

    # Muestra los datos de cada cuenta
    for cuenta in CUENTAS:
        print(f"Tipo de cuenta: {type(cuenta)}")
        print(f"Nombre: {cuenta.titular.nombre}")
        print(f"Edad: {cuenta.titular.edad}")
        print(f"DNI: {cuenta.titular.dni}")
        print(f"Cantidad: {cuenta.cantidad}")
        print("-" * 15)

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
