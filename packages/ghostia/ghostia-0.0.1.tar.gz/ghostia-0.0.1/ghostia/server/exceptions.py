from easy_validator import ValidationError
class ValueNotValid(Exception):
    def __init__(self,value=None,message="Valor no valido:"):
        super().__init__(message)
        self.value=value
    def __str__(self):
        return self.args[0]+"\n"+str(self.value)
class NeedRequeriment(Exception):
    """
    Esta excepcion es usada para manejar la falta de requerimientos en una funcion
    """
    def __init__(self,needs=[],message="Se necesitan especificar: ",):
        
        super().__init__()
        self.needs=needs
        self.message=message
    
    def __str__(self):
        from ghostia.server.helpers.text import array_repr
        
        return str(self.message+array_repr(self.needs))
class ParamsNotValid(Exception):
    """
    """
    def __init__(self,unvalids=[],message="parametros invalidos: "):
        super().__init__(message)
        self.unvalids=unvalids
    def __str__(self):

        return self.args[0]+str(self.unvalids)
class IntentNotValid(Exception):
    def __init__(self,unvalids=[],message="Intencion invalida: "):
        super().__init__(message)
        self.unvalids=unvalids
    def describe(self):
        """
        """

        if type(self.unvalids)!=dict:
            return f"La intención es tipo '{type(self.unvalids).__name__}' \
deberia ser 'dict'"

    def __str__(self):

        return self.args[0]+str(self.unvalids)+"\n"+self.describe()

class DontKnow(Exception):
    def __init__(self,name:str,message="Referencia desconocida"):
        super().__init__(message)
        self.name=name
class UnknowTechnique(Exception):
    def __init__(self,name:str):
        super().__init__()
        self.name=name
    def __str__(self):
        return f"Tecnica desconocida {self.name}"


class GeneratorRequired(Exception):
    def __init__(self,type):
        super().__init__()
        self.type=type
    def __str__(self):
        return f"Se necesita un generador para el tipo: {self.type.__name__}"

class Timeout(Exception):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return "Tiempo agotado"


class ReaderNotFound(Exception):
    """
    Excepcion aplicada al metodo worker.say cuando este tiene
    un modo diferente al normal y no tiene un reader para leer
    bien el texto que debe decir
    """
    def __init__(self,reader:str):
        super().__init__()
        self.reader=reader
    def __str__(self):
        return f"Reader '{self.reader}' no encontrado"
