from fastapi.testclient import TestClient

from app.main import app


def test_lista_todos_los_productos():
    with TestClient(app) as cliente:
        respuesta = cliente.get("/productos")

    assert respuesta.status_code == 200
    assert [producto["id"] for producto in respuesta.json()] == [1, 2, 3]


def test_devuelve_un_producto_existente():
    with TestClient(app) as cliente:
        respuesta = cliente.get("/productos/1")

    assert respuesta.status_code == 200
    assert respuesta.json() == {
        "id": 1,
        "nombre": "Estantería miniatura",
        "precio": "34.90",
    }


def test_devuelve_404_si_el_producto_no_existe():
    with TestClient(app) as cliente:
        respuesta = cliente.get("/productos/999")

    assert respuesta.status_code == 404
    assert respuesta.json() == {"detail": "Producto no encontrado"}
