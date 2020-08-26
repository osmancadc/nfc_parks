import eventlet
import socketio
import time
nfc = __import__('nfc_scan')

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

def wait_nfc():
	id = nfc.scan()
	sio.emit("NEW_DATA",{"id":id,"money":55000,"passport":"Platino full 4k 1080 2020 remix"})

@sio.on('connect')
def connect(sid, environ):
	print("New connection: ", sid)

@sio.on('ready')
def ready(sid, environ):
	wait_nfc()

@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
	print("Esperando en el puerto: 4567")
	eventlet.wsgi.server(eventlet.listen(('localhost', 4567)), app, log_output=False)