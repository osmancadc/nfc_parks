server = __import__ ('server_socket')
nfc = __import__('nfc_scan')
import socketio
import eventlet

sio = socketio.AsyncServer(cors_allowed_origins='*',async_mode='eventlet')
app = socketio.WSGIApp(sio)
socket = 4567

@sio.event
def connect(sid, environ):
	print('-> New connection',sid)

if __name__ == '__main__':
	print("Escuchando en el socket ",socket)
	eventlet.wsgi.server(eventlet.listen(('localhost', socket)), app, log_output=False)
	print("async socket")
	nfc.scan()