PYTHON := env/bin/python
PIP := env/bin/pip
MYPY := env/bin/mypy

env:
	python -m venv env

deps: env
	$(PIP) install -U -r requirements/base.txt

dev-deps: deps env
	$(PIP) install -U -r requirements/dev.txt

test:
	$(PYTHON) -m unittest discover -s tests

typecheck:
	$(MYPY) .

run:
	$(PYTHON) {{cookiecutter.name}}/app.py
