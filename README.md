# Tarea Extra Infografia

Tarea de guardar los landmarks de una imagen subida al servidor, guardandolos en una base de datos y permitiendo obtenerlos en formato JSON.

## Requerimientos

* Python +3.6

## Instalación

```bash
pip install -r requirements.txt
```
o
```bash
pip3 install -r requirements.txt
```

## Ejecución

```bash
python main.py
```
o
```bash
python3 main.py
```

## Uso

Acceder a la ruta http://127.0.0.1:8000/docs para ver la interfaz web.

Hay 2 endpoints:

* /upload_photo: (POST) Subir una imagen y guardar los landmarks en la base de datos.
* /get_landmarks: (GET) Obtener los landmarks de una imagen en formato JSON.