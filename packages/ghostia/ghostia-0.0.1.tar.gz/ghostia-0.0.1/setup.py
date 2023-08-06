from setuptools import setup,find_packages

setup(
	name="ghostia",
	packages=["ghostia","ghostia/server"],
	version="0.0.1",
	description="Plataforma de creacion de agentes inteligentes artificiales generales",
	author="Jesus Zerpa",
	author_email="support@zerpatechnology.com",
	url="https://zerpatechnology.com/projects/ghostia",
	keywords=["IA"],
	scripts=["ghostia/bin/ghostia"],
	entry_points={
		"console_scripts":[
			"ghostia = ghostia:create_superuser"
		]
	}
	)