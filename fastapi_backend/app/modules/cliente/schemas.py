from pydantic import BaseModel, Field
from typing import Optional
from .privilegiosClienteENUM import privilegiosCliente

class ClienteBase(BaseModel):
    id: int = Field(gt=0, example=1)
    nombre: str = Field(..., example = "John")
    apellido: str = Field(..., example = "Pérez")
    email: str = Field(..., example = "johnperez@yandex.ru")
    privilegio: privilegiosCliente = Field(..., example=privilegiosCliente.BASICO)
    activo: bool = True    

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(BaseModel):
    email: Optional[str] = Field(None, example="johnperez@yandex.ru")
    activo: Optional[bool] = None

class ClienteRead(ClienteBase):
    id: int