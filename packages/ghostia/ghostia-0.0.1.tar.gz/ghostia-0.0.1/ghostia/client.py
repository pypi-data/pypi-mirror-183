import socketio

# standard Python
sio = socketio.Client()


@sio.on('my_event')
def on_message(data):
    print('I received a message!',data)

sio.connect('http://localhost:5000/',namespaces=["/tasks"])
sio.emit("my_event",{"que":"hola mundo"},namespace="/tasks")
print("Mensaje enviado")