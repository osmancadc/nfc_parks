import socketio
import eventlet

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print('connect ', sid)
    sio.emit('NEW_CONNECTION',{"id":"01234567","money":56450,"passport":"Pasaporte platino full"})


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('localhost', 4567)), app)