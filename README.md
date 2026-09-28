# Flask App

Aplicación Flask que carga datos desde `app.json` y ofrece dos rutas HTTP.

## Requisitos y ejecución

Instala las dependencias:

    pip install -r req.txt

Ejecuta la aplicación desde la carpeta del proyecto:

    python app.py

La aplicación usa `app.json` del directorio actual y activa el modo de depuración.

## Ramas de Git

Las ramas del repositorio aún deben verificarse en Git; no se pueden deducir desde `app.py`. Para consultarlas:

    git branch -a

Añade aquí los nombres y propósitos de las ramas después de verificarlos.

## Rutas

Las dos rutas aceptan solicitudes `GET`.

| URL | Respuesta | Función |
|---|---|---|
| `/json/<mac>` | Texto plano | Busca `<mac>` en `app.json`, imprime los campos `Name`, `Protocolos` y `VLANs` en la consola del servidor, y devuelve `Name`. |
| `/servidor_1` | JSON | Devuelve datos fijos del dispositivo `0001`, incluidos IP, tipo, política y estado. |

### `GET /json/<mac>`

Reemplaza `<mac>` por una clave existente en `app.json`, por ejemplo:

    /json/0001

La entrada correspondiente debe incluir `Name`, `Protocolos` y `VLANs`. Si falta la clave o alguno de esos campos, la ruta puede producir un error. La respuesta HTTP solo contiene el valor de `Name`.

### `GET /servidor_1`

Devuelve un objeto JSON con información fija. En el código actual, `divice` está escrito así:

    {
      "0001": {
        "ip": "192.168.0.1",
        "divice": "Router",
        "policy": ["Ro", "Not Allowed", [0.2, 0.3, 0.5]],
        "status": true
      }
    }

## Mapa visual de rutas

    Cliente
      ├── GET /json/<mac>
      │     └── Busca datos en app.json
      │           ├── Imprime Name, Protocolos y VLANs en la consola
      │           └── Devuelve Name como texto plano
      │
      └── GET /servidor_1
            └── Devuelve datos fijos como JSON