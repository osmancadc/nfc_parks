import eventlet
import socketio
import time
import json 
nfc = __import__('nfc_scan')

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

def wait_nfc():
	id = nfc.scan()
	sio.emit("NEW_BAND",{"id":id})

@sio.on('connect')
def connect(sid, environ):
	print("New connection: ", sid)
	wait_nfc()

@sio.on('ready')
def ready(sid, environ):
	wait_nfc()

@sio.on('loading')
def ready(sid, environ):	
	time.sleep(3)
	sio.emit("DATA",{"id":environ['data']['id'],"money":54321,"passport":"Pasaporte full acces 10k"})


@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
	print("Esperando en el puerto: 4567")
	eventlet.wsgi.server(eventlet.listen(('localhost', 4567)), app, log_output=False)