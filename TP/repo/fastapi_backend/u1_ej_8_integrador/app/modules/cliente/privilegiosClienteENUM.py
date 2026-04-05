from enum import Enum

class privilegiosCliente(str, Enum):
    BASICO = "BASICO",
    PREMIUM = "PREMIUM",
    VIP = "VIP"