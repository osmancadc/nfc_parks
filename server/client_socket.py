import time
import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')
    sio.emit('ready',{})

@sio.event
def disconnect():
    print('disconnected from server')

@sio.event
def NEW_DATA(data):
    print(data)
    time.sleep(2)
    sio.emit('ready',{})


sio.connect('http://localhost:4567')
sio.wait()