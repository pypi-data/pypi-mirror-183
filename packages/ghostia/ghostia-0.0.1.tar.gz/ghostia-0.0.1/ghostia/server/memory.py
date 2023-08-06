class Memory:
    def __init__(self,worker):
        self.worker=worker
        self.objects=[]
        self.interest={}
        memory=self

        class Test:
            def __init__(self,name):
                from mongomantic import connect
                connect(name)
                memory.worker
            def __enter__(self):


                from mongomantic.core.database import MongomanticClient
                from pymongo import MongoClient
                
                self.database=MongomanticClient.database
                self.client=MongomanticClient.client
                if self.name not in mongo_client.database_names():
                    MongomanticClient.database=MongomanticClient.client.__getattr__(database)
                else:
                    raise Exception("Base de datos ya existe")

                
            def __exit__(self):
                MongomanticClient.database=self.database
                MongomanticClient.client=self.client
                self.client.drop_database(self.name)
        class Empty:
            def __init__(self,name):
                from mongomantic import connect
                connect(name)
                memory.worker
            def __enter__(self):


                from mongomantic.core.database import MongomanticClient
                from pymongo import MongoClient
                
                self.database=MongomanticClient.database
                self.client=MongomanticClient.client
                if self.name not in mongo_client.database_names():
                    MongomanticClient.database=MongomanticClient.client.__getattr__(database)
                else:
                    raise Exception("Base de datos ya existe")

                
            def __exit__(self):
                MongomanticClient.database=self.database
                MongomanticClient.client=self.client
        
        class Base:
            def __init__(self,name):
                self.name=name
            def __enter__(self):
                from mongomantic.core.database import MongomanticClient
                from pymongo import MongoClient
                
                self.database=MongomanticClient.database
                self.client=MongomanticClient.client
                
                self.client.admin.command('copydb',
                         fromdb=MongomanticClient.database,
                         todb=self.name)

                MongomanticClient.database=MongomanticClient.client.__getattr__(self.name)

            def __exit__(self):
                MongomanticClient.database=self.database
                MongomanticClient.client=self.client

        self.Test=Test
        self.Empty=Empty
        self.Base=Base
    def append(self,object):
        self.objects.append(object)
    def add(self,object):
        if object.id in self.interest:
            self.interest[object.id]+=1
        else:
            self.interest[object.id]=0
    def remember(self,name):
        from ghostia.server.models.entity import EntityRepository
        if name in self.worker.ctx["entities"]:
            owner:Entity=self.worker.ctx["entities"][entity]["owner"] #[my,your,their,us,this,any]

        possibles=EntityRepository.find(**{
            "name":entity,
            "owner":owner
            })
        
        if possibles:
            entity=self.worker.choose(possibles)[0]
            return entity
        
    def commit(self):
        from .models.entity import Entity,EntityRepository
        from .models.action import Action,ActionRepository
        from .models.help import Help,HelpRepository
        from .models.idea import Idea,IdeaRepository
        from .models.intent import Intent,IntentRepository
        from .models.word import Word,WordRepository
        from .models.knowledge import Knowledge,KnowledgeRepository
        from .models.language import Language,LanguageRepository
        from .models.location import Location,LocationRepository
        from .models.objective import Objective,ObjectiveRepository
        for elem in self.objects:
            locals()[elem.__name__+"Repository"].save(elem)
            

