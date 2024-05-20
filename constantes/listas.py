"""Listas constantes usadas en main"""

from typing import List
from clases.cuenta import Cuenta
from clases.cuenta_joven import CuentaJoven
from clases.cuenta_vip import CuentaVIP
from clases.plazo_fijo import PlazoFijo

# Lista donde se almacenan todas las cuentas
CUENTAS: List[Cuenta | CuentaJoven | CuentaVIP] = []

# Lista donde se almacenan los plazos fijos
PLAZOS_FIJOS: List[PlazoFijo] = []
