from typing import List, Optional
from .schemas import ClienteCreate, ClienteRead
from .privilegiosClienteENUM import privilegiosCliente

# Simulación de registros iniciales
db_clientes: List[ClienteRead] = [
    ClienteRead(id=1, nombre="Juan", apellido="Pérez", email="johnperez@yandex.ru", privilegio=privilegiosCliente.BASICO, activo=True),
    ClienteRead(id=2, nombre="Joaquín", apellido="López", email = "jqlpz@ok.w43", privilegio=privilegiosCliente.PREMIUM, activo=True)
]

id_counter = 3

def crear(data: ClienteCreate) -> ClienteRead:
    global id_counter
    id_counter += 1
    nuevo = ClienteRead(id=id_counter, **data.model_dump(exclude={"id"}))
    db_clientes.append(nuevo)
    return nuevo

def obtener_todos(skip: int = 0, limit: int = 10) -> List[ClienteRead]:
    return db_clientes[skip: skip + limit]

def obtener_por_id(id: int) -> Optional[ClienteRead]:
    for c in db_clientes:
        if c.id == id:
            return c
    return None

def dar_de_baja(id: int) -> Optional[ClienteRead]:
    for index, c in enumerate(db_clientes):
        if c.id == id:
            c_dict = c.model_dump()
            c_dict["activo"] = False
            actualizado = ClienteRead(**c_dict)
            db_clientes[index] = actualizado
            return actualizado
    return None

def promover_cliente(id: int) -> Optional[ClienteRead]:
    for index, c in enumerate(db_clientes):
        if c.id == id:
            c_dict = c.model_dump()
            if c_dict["privilegio"] == "BASICO":
                c_dict["privilegio"] = "PREMIUM"
            elif c_dict["privilegio"] == "PREMIUM":
                c_dict["privilegio"] = "VIP"
            elif c_dict["privilegio"] == "VIP":
                return c #Como el máximo para un cliente es VIP, no se puede promover más.
            actualizado = ClienteRead(**c_dict)
            db_clientes[index] = actualizado
            return actualizado
    return None

def degradar_cliente(id: int) -> Optional[ClienteRead]:
    for index, c in enumerate(db_clientes):
        if c.id == id:
            c_dict = c.model_dump()
            if c_dict["privilegio"] == "VIP":
                c_dict["privilegio"] = "PREMIUM"
            elif c_dict["privilegio"] == "PREMIUM":
                c_dict["privilegio"] = "BASICO"
            elif c_dict["privilegio"] == "BASICO":
                return c #Como el mínimo para un cliente es BASICO, no se puede degradar más.
            actualizado = ClienteRead(**c_dict)
            db_clientes[index] = actualizado
            return actualizado
    return None