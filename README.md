# nfc_parks

nfc_parks es el nombre generico que se le ha otorgado a este proyecto, el cual es encargado de una administracion electronica de  un usuario en un determinado parque, a traves de esta herramienta, que utiliza la tecnologia nfc, los parques de diversiones serán capaces de administrar todo lo relacionado con sus vistantes, y hacer uso de los datos de la mejor forma posible.


## Instalacion del servidor

Use el administrador de paquetes pip para instalar el servidor

```bash
	cd server/
	pip3 install -r requirements.txt
	python3 main.py
```

## Crear un cliente de prueba

```python
import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.on('new connection')
def new_connection(data):
    print(data)

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:4567')
sio.wait()
```

## Contributing
Pull requests unicamente son autorizados por los creadores del software [Osmancadc] & [yderfre]

## License
[BSL-1.0](https://choosealicense.com/licenses/bsl-1.0/)