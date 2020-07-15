default: ci

env:
	python -m venv env

deps: env
	env/bin/pip install -U -r requirements/base.txt

dev-deps: deps env
	env/bin/pip install -U -r requirements/dev.txt

test:
	env/bin/python -m unittest discover -s tests

typecheck:
	env/bin/mypy .

fmtcheck:
	env/bin/black --check {{cookiecutter.name}} tests

lint:
	env/bin/pylint {{cookiecutter.name}} tests

ci: dev-deps fmtcheck typecheck test lint

run:
	env/bin/python {{cookiecutter.name}}/app.py

clean:
	rm -rf env .mypy_cache
