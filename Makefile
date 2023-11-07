COMP = python
PATH = "C:\Users\dante\Documents\ACADEMICO\Cursos\Django - Crie aplicações em Python\Templates e boas práticas\manage.py"
VENV = "C:\Users\dante\Documents\ACADEMICO\Cursos\Django - Crie aplicações em Python\Templates e boas práticas\venv\Scripts\activate"

CMD = $(COMP) $(PATH)

migrate:
	$(CMD) makemigrations
	$(CMD) migrate

runserver:
	$(CMD) runserver

venv:
	$(VENV)