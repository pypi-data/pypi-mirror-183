import inspect

class Channel:

    def __init__(self,name,batch_size=100):
        self.connectors=[]
        self.outputs=[]
        self.batch_size=batch_size

    def connect(self,connector):
        self.connectors.append(connector)
    def disconnect(self,connector):
        self.connectors.remove(connector)
    async def push(self,data):
        """
        Se lanza los connectores cuando se empuja datos al canal
        """
        for connector in self.connectors:
            if inspect.iscoroutinefunction(connector):
                await connector(data)
            else:
                connector(data)
        if len(self.outputs)==self.batch_size:
            del self.outputs[0]
        self.outputs.append(data)

class Channeler:
    """
    Se trata de un canalizador de datos
    esto consiste en detectar cuales son los inputs existentes
    y que tipos de datos estos aceptan
    entonces concetamos estos inputs a nuestro canalizador y les
    enviamos el buffer de datos correspondiente

    ¿Qué son y para qué sirven?
En pocas palabras, una canalización de datos es un conjunto de acciones y tecnologías que enrutan datos sin procesar desde un origen a un destino. Las canalizaciones de datos a veces se denominan conectores de datos.

Las canalizaciones de datos constan de estos componentes: una fuente, un paso de transformación de datos y un destino.
    """
    channels={}
    
    def __init__(self,worker:"Worker",batch_size=100):
        from ghostia.server.composer import composer
        self.logger=composer.logger("channeler")
        self.worker=worker
        self.transformers={}
        self.batch_size=batch_size
    def __getitem__(self,name):
        if name not in self.channels:
            self.logger.warning(f"Canal '{name}' creado de forma automatica")
            self.create_channel(name)
        
        return self.channels[name]
    def __setitem__(self,name,data):
        self[name].push(data)

    def create_channel(self,name):
        """
        """
        self.channels[name]=Channel(name)
    def input(self,connector:callable):
        """
        añade una entrada, (DESTINO)

        al connector se le pasa un objeto el cual es
        el que nos da la libreria que manipula este tipo
        de datos, con sus datos dentro, ya le tocara al
        connector deducir la libreria empleada para trabajar
        con este tipo de datos
        """
        for channel  in self.channels:
            if channel==connector.__annotations__["data"]:
                self.channels[channel].connect(connector)

    async def buffer(self,file,channel="Text",readlines=False)->str:
        """
        (ORIGEN)
        """
        
        transformation=await self.apply_transform(channel,file)
        if not file.closed:
            file.close()
     
        return channel
    async def apply_transform(self,channel,file):
        before_transfrom=None
        if file.mode=="r":#es un archivo de texto
            for transformer in self.transformers[channel]:
                if inspect.iscoroutinefunction(transformer):
                    before_transfrom=await transformer(file,before_transfrom)
                else:
                    before_transfrom=transformer(file,before_transfrom)
            return before_transfrom




    def transform(self,channel,transformer):
        """
        """
        if channel not in self.transformers:
            self.transformers[channel]=[]    
        self.transformers[channel].append(transformer)

    async def __call__(self,buffer,channel="Text"):
        transformation=await self.buffer(buffer,channel=channel)
        
        self.channels[channel].push(transformation)
        
        return self.channels[channel].outputs[-1]
