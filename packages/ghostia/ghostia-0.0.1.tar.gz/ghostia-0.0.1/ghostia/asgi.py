
from ghostia.server.composer import composer
from ghostia.server import app,socketio,sio,run,global_queue
import click

import uvicorn,threading
import signal


def sigterm_handler(_signo, _stack_frame):
    # Raises SystemExit(0):
    with open("FINALIZANDO.txt","w") as f:
        f.write("oooooo")
    sys.exit(0)

signal.signal(signal.SIGTERM, sigterm_handler)

print("JJJJJJJJJJ")
t=threading.Thread(target=run,args=(global_queue,))
t.daemon = True
t.start()

if __name__=="__main__":
    import threading
    """
    {action:leer, message:'este mensaje'} #leer en voz alta
    {action:interpretar, message:'este mensaje'} #realizar accion en base a la lectura
    {action:recibir_informacion, message:'este mensaje'} #guardar la informacion suministrada
    {action:responder, message:'este mensaje'} #dar una respuesta a la solicitud
    """

    
    
    app = socketio.ASGIApp(sio, app, static_files={
        '/': 'app.html',
    })

    uvicorn.run("asgi:app", host='127.0.0.1', port=5000,reload=True)
    #app.run(debug=True)
    #socketio.run(app,debug=True)
