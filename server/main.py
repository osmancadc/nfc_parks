import socketio
import eventlet

sio = socketio.AsyncServer(cors_allowed_origins='*',async_mode='eventlet')
app = socketio.WSGIApp(sio)
socket = 4567


@sio.event
def connect(sid, environ):
    print('connect ', sid)
    sio.emit('NEW_BAND', {"id": "1234567"})
    # sio.emit('NEW_DATA', {"id": "02468", "money": 40000,
    #                       "passport": "Pasaporte platino full"})
    # sio.emit('NEW_READ', {"id": "369", "money": 90000,
    #                       "passport": "Pasaporte platino full"})


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('localhost', 4567)), app)
