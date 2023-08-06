def step(tags=[],validator=None,test=None,reverse=None,solvers=[],statetor=None,kind="GET"):
    """
    Decorador para los metodos de las skill y methods
    * statetor: un estator es una funcion encargada de reportar el o los attributos que 
    describe en el estado del mundo el valor devuelto por una accion
    """
    from .composer import  composer,Step
    
    def register(result,session,step,status=None):
        from ghostia.server.models.action import register
        session=composer.worker.session_current
        worker=composer.worker
        print(">>>>>>>>>",instance,result)
        register(
            instance.callback,
            status=status,
            session=session.name,step=session.step,
            result=result,tags=tags,validator=validator,
            test=test,reverse=reverse,solvers=solvers,kind=kind)


    
    instance=Step(register,validator=validator,test=test,solvers=solvers)
    return instance.executor
