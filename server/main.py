import socketio
import eventlet

sio = socketio.Server()
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print('connect ', sid)
    sio.emit('new connection',{"data":"Nueva conexion desde python"})


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('localhost', 4567)), app)