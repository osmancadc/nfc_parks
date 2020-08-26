import socketio
import eventlet

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print('connect ', sid)
    sio.emit('NEW_BAND',{"id":"0123456"})
    


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('localhost', 4567)), app)