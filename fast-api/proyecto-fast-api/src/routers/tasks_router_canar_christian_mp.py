from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

tasks_router = APIRouter()


class MascotaCreate(BaseModel):
    """Lo que el cliente envía para registrar una mascota. Sin id: lo asigna el servidor."""
    nombre: str = Field(min_length=3, max_length=100)
    descripcion: str | None = None
    urgencia: str = "media"
    etiquetas: list[str] = Field(default_factory=list)

class MascotaRead(BaseModel):
    """Lo que el servidor expone al leer una mascota. Incluye campos calculados por el servidor."""
    id: int
    nombre: str
    descripcion: str | None
    urgencia: str
    etiquetas: list[str]
    adoptada: bool


class MascotaUpdate(BaseModel):
    """Lo que el cliente envía para actualizar. TODOS los campos son opcionales."""
    nombre: str | None = Field(default=None, min_length=3, max_length=100)
    descripcion: str | None = None
    urgencia: str | None = None
    etiquetas: list[str] | None = None
    adoptada: bool | None = None


MASCOTAS: list[dict] = [
    {"id": 1, "nombre": "Firulais", "descripcion": None, "urgencia": "media", "etiquetas": ["perro", "labrador"], "adoptada": False},
    {"id": 2, "nombre": "Mishi", "descripcion": None, "urgencia": "alta", "etiquetas": ["gato", "siames"], "adoptada": False},
]
SIGUIENTE_ID = len(MASCOTAS) + 1

@tasks_router.post("/mascotas", response_model=MascotaRead)
def create_mascota(mascota: MascotaCreate) -> dict:
    global SIGUIENTE_ID
    nueva_mascota = {
        "id": SIGUIENTE_ID,
        "adoptada": False,
        "notas_internas": "registrada desde la API",  # campo interno, nunca debería salir al cliente
        **mascota.model_dump(),
    }
    MASCOTAS.append(nueva_mascota)
    SIGUIENTE_ID += 1
    return nueva_mascota


@tasks_router.get("/mascotas", response_model=list[MascotaRead])
def list_mascotas() -> list[dict]:
    return MASCOTAS

@tasks_router.patch("/mascotas/{mascota_id}")
def update_mascota(mascota_id: int, update: MascotaUpdate) -> dict:
    for mascota in MASCOTAS:
        if mascota["id"] == mascota_id:
            cambios = update.model_dump(exclude_unset=True)
            mascota.update(cambios)
            return mascota
    return {"error": "Mascota no encontrada"}

@tasks_router.post("/mascotas/from-model")
def create_from_model(mascota: MascotaCreate) -> dict:
    global SIGUIENTE_ID
    # model_dump(): instancia de Pydantic -> dict plano de Python
    data = mascota.model_dump()
    nueva_mascota = {"id": SIGUIENTE_ID, "adoptada": False, **data}
    MASCOTAS.append(nueva_mascota)
    SIGUIENTE_ID += 1

    # model_validate(): dict de Python -> instancia validada de Pydantic
    validada = MascotaRead.model_validate(nueva_mascota)
    return validada.model_dump()


@tasks_router.get("/mascotas/{mascota_id}/raw-vs-validated")
def compare_raw_validated(mascota_id: int) -> dict:
    raw = next((m for m in MASCOTAS if m["id"] == mascota_id), None)
    if raw is None:
        return {"error": "no encontrada"}

    # model_validate lanza una excepción si el dict no cumple el schema de MascotaRead
    validada = MascotaRead.model_validate(raw)

    return {
        "raw_dict": raw,
        "validated_model_dump": validada.model_dump(),
        "validated_model_dump_json": validada.model_dump_json(),
    }

@tasks_router.delete("/mascotas/{mascota_id}")
def delete_mascota(mascota_id: int) -> dict:
    for index, mascota in enumerate(MASCOTAS):
        if mascota["id"] == mascota_id:
            eliminada = MASCOTAS.pop(index)

            return {
                "message": "Mascota eliminada correctamente",
                "deleted_mascota": eliminada
            }
    raise HTTPException(
        status_code=404,
        detail="Mascota no encontrada"
    )

@tasks_router.get("/mascotas/{mascota_id}", response_model=MascotaRead)
def get_mascota_by_id(mascota_id: int) -> dict:
    for mascota in MASCOTAS:
        if mascota["id"] == mascota_id:
            return mascota
    # El raise va FUERA del for: solo se lanza si ninguna mascota coincidió
    raise HTTPException(
        status_code=404,
        detail="Mascota no encontrada"
    )
