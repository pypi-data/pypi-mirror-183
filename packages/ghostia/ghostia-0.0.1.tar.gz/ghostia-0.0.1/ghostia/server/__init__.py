import json,os
import socketio
from quart import Quart,jsonify
from quart_cors import  cors
from mongomantic import connect
from dotenv import dotenv_values
from quart.json import JSONEncoder
from queue import  Queue
import imp
from .routes import router, router_actions, router_entity, router_language,\
	router_methods, router_goals, router_skills, router_tasks, router_words,\
	router_states,router_reasoning,router_testers, router_grammar,router_knowledges,\
	router_training

global_queue=Queue()
BASE_DIR=os.path.abspath(os.path.dirname(__file__).replace(" ","\/")+"/../")+"/"
os.environ["BASE_DIR"]=BASE_DIR

os.environ.update(dotenv_values(BASE_DIR+".env"))
connect(os.environ["MONGO_URI"],os.environ["MONGO_URI"].split("/")[-1])



from ghostia.server.composer import composer
from mongomantic.core.errors import DoesNotExistError
composer.queue=global_queue

class MyJSONEncoder(JSONEncoder):
    def default(self, o):
        from datetime import time,datetime,date
        from enum import Enum
        from bson.objectid import ObjectId
        from mongomantic import  BaseRepository, MongoDBModel
        from dataclasses import asdict,is_dataclass
        from ghostia.server.skills.read.lib import  Reading
        if isinstance(o, datetime):
            return o.isoformat()
        elif isinstance(o, time):
            return o.isoformat()

        elif isinstance(o, Enum):
        	return o.value
        elif isinstance(o, ObjectId):

        	return str(o)
        elif is_dataclass(o):
        	return {**{"id":o.id},**asdict(o)}
        elif isinstance(o, MongoDBModel):
        	return {**{"id":o.id},**o.dict()}
        elif callable(o):
        	return o()
        elif isinstance(o,Reading):
        	return o.todict()
       	else:
       		
       		print(type(o))
        return super().default(o)

class MyQuart(Quart):
    json_encoder = MyJSONEncoder

app=MyQuart(__name__)

sio = socketio.AsyncServer(async_mode='asgi')





app = cors(app,allow_origin="*")
app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]
app.config["BASE_DIR"]=BASE_DIR

app.register_blueprint(router,url_prefix="/json/v1")
app.register_blueprint(router_actions,url_prefix="/json/v1")
app.register_blueprint(router_entity,url_prefix="/json/v1")
app.register_blueprint(router_language,url_prefix="/json/v1")
app.register_blueprint(router_methods,url_prefix="/json/v1")
app.register_blueprint(router_goals,url_prefix="/json/v1")
app.register_blueprint(router_skills,url_prefix="/json/v1")
app.register_blueprint(router_tasks,url_prefix="/json/v1")
app.register_blueprint(router_words,url_prefix="/json/v1")
app.register_blueprint(router_states,url_prefix="/json/v1")
app.register_blueprint(router_reasoning,url_prefix="/json/v1")
app.register_blueprint(router_testers,url_prefix="/json/v1")
app.register_blueprint(router_grammar,url_prefix="/json/v1")
app.register_blueprint(router_knowledges,url_prefix="/json/v1")
app.register_blueprint(router_training,url_prefix="/json/v1")


for elem in os.listdir("server/skills/"):
	if os.path.exists(f"server/skills/{elem}/routes/__init__.py"):
		route=imp.load_source(elem,f"server/skills/{elem}/routes/__init__.py").router
		app.register_blueprint(route,url_prefix=f"/skills/{elem}")


composer.objects["sio"]=sio
composer.objects["app"]=app

from ghostia.server.models.entity import Entity,EntityRepository


from ghostia.server.websockets import *
from ghostia.server.routes import *

async def routines(worker,queue):
	print("ROUTINES")
	await asyncio.gather(
		worker.live(queue),
		#worker.listen() #reconocimiento de voz
		)

def run(queue):
	"""
	Preparamos el worker para inicializarse
	"""

	from .composer import composer
	import asyncio

	worker=composer.load_worker("developer")({
		"interface":["audio"]
		})
	
	composer.worker=worker
	asyncio.run(routines(worker,queue))