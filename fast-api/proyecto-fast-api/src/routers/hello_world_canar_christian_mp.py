from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Mensaje(BaseModel):
    texto: str
    prioridad: int = 1
    campo_interno: str

@router.get("/")
def read_root() -> dict[str, str]:
    return {"mensaje": "Bienvenido al refugio de mascotas con FastAPI + uv",
            "autor": "Christian Cañar",
            "version": "0.1.0"}

@router.get("/christian")
def endpoint_christian() -> Mensaje:
    return Mensaje(texto="Hola Christian, ¿listo para adoptar?", campo_interno="desde christian link")

@router.get("/canar", response_model=Mensaje)
def endpoint_canar():
    return {"texto": "Hola Cañar, Firulais te espera",
            "prioridad": 5,
            "campo_interno": "imprime desde endpoint canar"}

@router.get("/campo-extra", response_model=Mensaje)
def endpoint_campo_extra():
    return {"texto": "Hola Cañar, Mishi te espera",
            "prioridad": 5,
            "campo_interno": "si debe salir incluido en el modelo",
            "campo_extra": "no deberia salir"}
