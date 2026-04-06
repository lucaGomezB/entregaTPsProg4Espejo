from fastapi import APIRouter, HTTPException, Path, Query, status
from typing import List
from . import schemas, services

router = APIRouter(prefix="/clientes", tags = ["/clientes"])

# ---------------------------------------------------------
# ALTA DE CLIENTE
# Método: POST | Endpoint: /clientes | Estado: 201 Created
# ---------------------------------------------------------

@router.post("/", response_model=schemas.ClienteRead, status_code=status.HTTP_201_CREATED)
def alta_cliente(cliente: schemas.ClienteCreate):
    return services.crear(cliente)

# Listar Clientes
@router.get("/", response_model=List[schemas.ClienteRead], status_code=status.HTTP_200_OK)
def listar_clientes(skip: int = Query(0, ge=0), limit: int = Query(10, le=50)):
    return services.obtener_todos(skip, limit)

# ---------------------------------------------------------
# DETALLE DE CLIENTE
# Método: GET | Endpoint: /clientes/{id} | Estado: 200 OK
# ---------------------------------------------------------

@router.get("/{id}", response_model=schemas.ClienteRead, status_code=status.HTTP_200_OK)
def detalle_cliente(id: int = Path(..., gt=0)):
    cliente = services.obtener_por_id(id)
    if not cliente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado")
    return cliente

# ---------------------------------------------------------
# ACTUALIZACIÓN (Reemplazo Total)
# Método: PUT | Endpoint: /clientes/{id} | Estado: 200 OK
# ---------------------------------------------------------

@router.put(
    "/{id}", response_model=schemas.ClienteRead, status_code=status.HTTP_200_OK
)
def actualizar_cliente(cliente: schemas.ClienteCreate, id: int = Path(..., gt=0)):
    # Usamos ClienteCreate porque es un reemplazo total (exige todos los campos)
    actualizado = services.actualizar_total(id, cliente)
    if not actualizado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado"
        )
    return actualizado


# ---------------------------------------------------------
# ACTUALIZACIÓN (Promoción de Privilegio)
# Método: PUT | Endpoint: /clientes/{id} | Estado: 200 OK
# ---------------------------------------------------------

@router.put("{id}/promover", response_model=schemas.ClienteRead, status_code=status.HTTP_200_OK)
def promover_cliente(id: int = Path(..., gt=0)):
    promovido = services.promover_cliente(id)
    if not promovido:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado o ya es VIP"
        )
    return promovido


# ---------------------------------------------------------
# ACTUALIZACIÓN (Degradación de Privilegio)
# Método: PUT | Endpoint: /clientes/{id} | Estado: 200 OK
# ---------------------------------------------------------

@router.put("{id}/degradar", response_model=schemas.ClienteRead, status_code=status.HTTP_200_OK)
def degradar_cliente(id: int = Path(..., gt=0)):
    degradado = services.degradar_cliente(id)
    if not degradado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail = "No se encontró el cliente o ya es BASICO"
        )
    return degradado
# ---------------------------------------------------------
# BORRADO LÓGICO
# Método: PUT | Endpoint: /clientes/{id}/desactivar | Estado: 200 OK
# ---------------------------------------------------------

@router.put("/{id}/desactivar", response_model=schemas.ClienteRead, status_code=status.HTTP_200_OK)
def borrado_logico(id: int = Path(..., gt=0)):
    desactivado = services.desactivar(id)
    if not desactivado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado"
        )
    return desactivado