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