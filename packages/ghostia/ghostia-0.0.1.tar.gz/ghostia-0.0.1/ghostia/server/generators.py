from ghostia.server.composer import composer
from ghostia.server.models.entity import  EntityRepository
from ghostia.server.models.wish import  WishRepository
import os
@composer.generator(str)
def generate(worker,name,options={},timeout=10):
	#Importate saber si tenemos deseos ya que en el deseo puede estar 
	#la  entidad a la que vamos a pasar por parametro incluso la accion
	#los deseos basicamente son acciones en espera de poder ser ejecutadas
	wish=list(WishRepository.find(**{"action":name}))
	if len(wish):
		return wish.params[name]
	#las entidades aveces puede ser pasadas a acciones en este caso esta entidad 
	#es basicamente el target/parametro de la accion
	entity=EntityRepository.find_one(name=name)
	print("GGGGGGGGGGGGGGGGGGGGGGGG",entity)
	
	if entity and "action" in entity and entity["action"]:
		return entity
		

@composer.generator(str)
def  generate(worker,name,options={"is_sentence":True,"max_length":50,"per_word":8,"words":5},timeout=100):
	
	cache_words=[]
	with open(os.environ["BASE_DIR"]+"files/cache/words.txt") as f:
		content=f.read().strip()
		if content:
			cache_words=[x.title() for x in content.split(",")]

	if len(cache_words)==0:

		from ghostia.server.models.word import  WordRepository
		from ghostia.server.models.rule import  RuleRepository
		import re
		from ghostia.server.skills.read.lib.nlp import Nlp

		nlp=Nlp(RuleRepository,WordRepository,init_components=True,mode="debug")

		rules=list(RuleRepository.find())
		rule=worker.choose(rules,random=True)[0]
		
		tokens=nlp.rule2tokens(rule.formule)
	sentence=[]
	grammar=[]

	# arreglar las notaciones que estan separadas de sus siglas raiz
	# crear validador de siglas es decir pasar el grammar a el componente de sigla raiz y que esta diga si es o no

	for token in tokens:
		regx = re.compile("^"+token, re.IGNORECASE)
		if len(cache_words)==0:
			words=list(WordRepository.find(
				**{"grammar":{"$in":[regx]}
				 }))
			
			print("YYYYYYY",[[word.word,word.grammar] for word in words][:100])
			print("ggggg",token)
		else:
			words=list(WordRepository.find(
				**{"grammar":{"$in":[regx]},
				 "word":{"$in":cache_words}}))

		word=worker.choose(words,random=True)[0]
		for gra in word.grammar:
			if token in gra:
				grammar.append(gra)
				break

		sentence.append(word.word)
	print("uuuuuuu",tokens)
	print("kkkkkkk",rule.formule)
	print("vvvvvvvvvvvv",grammar)
	print("ZZZZZZZZZZZZ",sentence)
	return " ".join(sentence)

		



@composer.generator(str,9)
def generate(worker,name,options={"is_sentence":True,"max_length":50,"per_word":8,"words":5},timeout=100):
	#Importate saber si tenemos deseos ya que en el deseo puede estar 
	#la  entidad a la que vamos a pasar por parametro incluso la accion
	#los decesos basicamente son acciones en espera de poder ser ejecutadas
	from ghostia.server.models.word import  WordRepository

	from ghostia.server import exceptions
	import time

	#Esto es asi porque algo tan random no se puede converger en tan poco tiempo como para ser usado
	#ver lista de palabras conocidas
	#ver si el orden de las palabras conocidas son validas para alguna regla


	vocabulary="bcdfghjklmnñpqrstvwxyz"
	vocals="aeiouaeiouaeiouáéíóúü"
	silabas=[]
	


	with open(os.environ["BASE_DIR"]+"files/text/silabas.txt") as f:
		silabas=f.read().split(",")

	restriciones=["wp"]
	if options["is_sentence"]:
		import random

		
		
		validator={}
		tiempo=time.time()
		while time.time()-tiempo<timeout:
			n_words=random.randrange(2,5)
			l=[]
			for x in range(0,n_words):
				length_word=random.randint(0,options["per_word"])

				cadena=""
				
				for i in range(0,length_word):					
					ch=random.randint(0,len(silabas)-1)
					cadena+=silabas[ch]
				validator[cadena.title()]=0
				l.append(cadena.title())
			
			

			words=WordRepository.find(**{"word":{"$in":l}})
			for word in words:
				if word.word in validator:
					validator[word.word]+=1

			if 0 not in validator.values():  

				with open(os.environ["BASE_DIR"]+"files/text/words.txt") as f:
					with open(os.environ["BASE_DIR"]+"files/text/words.txt","w") as f2:
						words=f.read().split(",")
						words.extend(validator.keys())
						words=set(words)
						f2.write(",".join(words))

				return " ".join(l)
			else:
				l=[]

		raise exceptions.Timeout()

	elif "max_length" in options:
		max_length=randint.randint(0,options["max_length"])
		candena=""
		for x in range(0,max_length):
			ch=(vocabulary+" ")[randrange.randint(0,len(vocabulary)+1)]
			cadena+=ch
	else:
		max_length=randint.randint(0,100)
		candena=""
		for x in range(0,max_length):
			ch=(vocabulary+" ")[randrange.randint(0,len(vocabulary)+1)]
			cadena+=ch
		return cadena





