import asyncio,pytest
async def run_cli(fn):
    from cli.main import Cli
    cli=Cli()
    await fn(cli)

async def run_app(fn):
    from ghostia.server import app,composer
    await fn(app,composer)
    app.run()

def create_app(test_config=None):
    from ghostia.server import app,composer
    app.composer=composer
    return app

def create_app2(test_config=None):
    from quart import  Quart
    app=Quart(__name__)
    return app

from functools import wraps

class Decorator:
    def __getattr__(self,name):
        
        def wrapper(function):
            @wraps(function)
            def wrapper2(*args,**kwargs):             
                loop=asyncio.new_event_loop()
                try:
                    loop.run_until_complete(function(*args,**kwargs))
                finally:
                    loop.close()
            return getattr(pytest.mark,name)(wrapper2)
        return wrapper
decorator=Decorator()