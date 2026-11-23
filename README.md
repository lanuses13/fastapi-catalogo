# API de catálogo de miniaturas

Demo de backend con Python y FastAPI inspirada en Dementeamanos. El catálogo contiene tres productos ficticios guardados en memoria. El precio representa euros y viaja como texto decimal.

## Ejecutar en macOS

Abre esta carpeta en VS Code y ve a **Terminal → Nueva terminal**. Usa Python 3.10 o posterior.

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m uvicorn app.main:app --reload
```

Abre la [documentación interactiva](http://127.0.0.1:8000/docs). Despliega una ruta y pulsa **Try it out → Execute**. Para detener el servidor, pulsa **Control + C**.

| Petición | Resultado esperado |
|---|---|
| `GET /productos` | 200 con tres productos |
| `GET /productos/1` | 200 con la estantería miniatura |
| `GET /productos/999` | 404 con «Producto no encontrado» |
| `GET /productos/hola` | 422 porque el identificador debe ser un número entero |

## Ejecutar las pruebas

Desde la raíz del proyecto, con el entorno activado, ejecuta `python -m pytest -q`. Las pruebas usan el cliente de FastAPI y pueden ejecutarse con el servidor detenido.

## Leer el código

- `app/main.py` contiene el modelo de respuesta `Producto`, los datos de ejemplo y las dos rutas.
- `tests/test_productos.py` comprueba el listado, una ficha existente y el error 404.
- `requirements.txt` declara las dependencias del servidor. `requirements-dev.txt` añade las de pruebas.

En `@app.get("/productos")`, el decorador conecta esa URL con la función siguiente. La anotación `producto_id: int` hace que FastAPI valide el valor recibido. La función busca el identificador y devuelve 404 cuando el número es válido pero no existe en el catálogo. En `/docs` puedes comprobar el contrato que genera FastAPI.
