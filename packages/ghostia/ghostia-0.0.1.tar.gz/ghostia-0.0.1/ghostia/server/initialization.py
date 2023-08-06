World=EntityManager.get("World")
Web=EntityManager.get("Web")
Web.inherit(World)
try:
	EntityRepository.get(alias="path")
except DoesNotExistError as e:
	entity=Entity(**{
		"name":"Path",
		"codename":"Path",
		"alias":["path"],
		})
	entity=EntityRepository.save(entity)
try:
	EntityRepository.get(alias="content")
except DoesNotExistError as e:
	entity=Entity(**{
		"name":"Content",
		"codename":"Content",
		"alias":["content"],
		})
	entity=EntityRepository.save(entity)
