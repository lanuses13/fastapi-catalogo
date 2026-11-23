from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Producto(BaseModel):
    id: int
    nombre: str
    precio: str


PRODUCTOS = {
    1: Producto(id=1, nombre="Estantería miniatura", precio="34.90"),
    2: Producto(id=2, nombre="Alacena miniatura", precio="49.00"),
    3: Producto(id=3, nombre="Escritorio miniatura", precio="29.50"),
}

app = FastAPI(
    title="API de catálogo de miniaturas",
    description="Demo de un catálogo de solo lectura con datos ficticios.",
    version="1.0.0",
)


@app.get("/productos", tags=["Catálogo"])
def listar_productos() -> list[Producto]:
    """Devuelve todos los productos del catálogo."""
    return list(PRODUCTOS.values())


@app.get(
    "/productos/{producto_id}",
    tags=["Catálogo"],
    responses={404: {"description": "Producto no encontrado"}},
)
def obtener_producto(producto_id: int) -> Producto:
    """Busca un producto por su identificador."""
    producto = PRODUCTOS.get(producto_id)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto
