import socketio
import eventlet

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)
socket = 4567

@sio.event
def connect(sid, environ):
    print('connect ', sid)
    
def new_emit(event,data):
    sio.emit(event,data)

def open_socket():
    print("Escuchando en el socket ",socket)
    eventlet.wsgi.server(eventlet.listen(('localhost', socket)), app)
